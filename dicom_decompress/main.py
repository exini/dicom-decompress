import sys
import argparse
import pydicom

ts_skip = [
    '1.2.840.10008.1.2.1',
    '1.2.840.10008.1.2',
    '1.2.840.10008.1.2.2',
    '1.2.840.10008.1.2.1.99',
]

ts_decompress = [
    '1.2.840.10008.1.2.5',
    '1.2.840.10008.1.2.4.50',
    '1.2.840.10008.1.2.4.51',
    '1.2.840.10008.1.2.4.57',
    '1.2.840.10008.1.2.4.70',
    '1.2.840.10008.1.2.4.80',
    '1.2.840.10008.1.2.4.81',
    '1.2.840.10008.1.2.4.90',
    '1.2.840.10008.1.2.4.91',
    '1.2.840.10008.1.2.4.92',
    '1.2.840.10008.1.2.4.93',
]

pi_rgb = 'RGB'
pi_palette = 'PALETTE COLOR'

supported_photometric_interpretations = [
    'YBR_FULL',
    'YBR_FULL_422',
    pi_palette,
]


def decompress(dataset, ts):
    try:
        dataset.decompress()
        sys.stdout.write(f"Decompression successful from transfer syntax UID {ts}\n")
    except:
        try:
            dataset.decompress('gdcm')
            sys.stdout.write(f"Decompression successful from transfer syntax UID {ts}\n")
        except Exception as e:
            sys.stderr.write(f'Decompression of transfer syntax {ts} failed. Reason: {e}\n')


def transcode(dataset, pi):
    try:
        arr = dataset.pixel_array
        if pi == pi_palette:
            rgb = pydicom.pixel_data_handlers.util.apply_color_lut(arr, dataset)
            dataset.SamplesPerPixel = 3
            dataset.PlanarConfiguration = 0
        else:
            rgb = pydicom.pixel_data_handlers.convert_color_space(arr, pi, pi_rgb)
        rgb = (rgb / 256).astype('uint8') if rgb.dtype == 'uint16' else rgb
        dataset.PixelData = rgb.tobytes()
        dataset.PhotometricInterpretation = pi_rgb
        dataset.BitsAllocated = 8
        dataset.BitsStored = 8
        dataset.HighBit = 7
        sys.stdout.write(f"Transcoding successful from photometric interpretation {pi}\n")
    except Exception as e:
        sys.stderr.write(f'Transcoding from {pi} to RGB failed. Reason: {e}\n')


def main():
    parser = argparse.ArgumentParser(description='Decompress and transcode pixel data in DICOM files.')
    parser.add_argument('in_file', type=argparse.FileType('rb'), help='Input DICOM file name')
    parser.add_argument('out_file', type=argparse.FileType('wb'), help='Output file name')
    parser.add_argument('--transcode', dest='transcode', action='store_const',
                        const=True, default=False,
                        help='If Photometric Interpretation is not RGB, try transcoding it to RGB. By default, transcoding will not be attempted.')

    args = parser.parse_args()

    try:
        dataset = pydicom.dcmread(args.in_file, force=True)

        if 'TransferSyntaxUID' not in dataset.file_meta:
            dataset.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian

        if 'PhotometricInterpretation' not in dataset:
            dataset.PhotometricInterpretation = 'MONOCHROME2'

        ts = dataset.file_meta.TransferSyntaxUID
        pi = dataset.PhotometricInterpretation

        if ts in ts_decompress:
            decompress(dataset, ts)
        elif ts in ts_skip:
            sys.stdout.write(f"Transfer syntax UID {ts} is uncompressed\n")
        else:
            sys.stdout.write(f"Transfer syntax UID {ts} not supported\n")

        if args.transcode and pi in supported_photometric_interpretations:
            transcode(dataset, pi)

        pydicom.dcmwrite(args.out_file, dataset, write_like_original=False)

    except Exception as e:
        sys.stderr.write(f'Error in DICOM read/write: {e}\n')
        exit(1)


if __name__ == "__main__":
    main()
