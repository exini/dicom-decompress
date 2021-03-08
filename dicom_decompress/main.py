import sys
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

supported_photometric_interpretations = [
    'YBR_FULL',
    'YBR_FULL_422',
]

rgb_photometric_interpretation = 'RGB'


def decompress(dataset, ts):
    try:
        dataset.decompress('pylibjpeg')
    except Exception as e:
        sys.stderr.write(f'Decompression of transfer syntax {ts} failed. Reason: {e}\n')


def transcode(dataset, pi):
    try:
        rgb = pydicom.pixel_data_handlers.convert_color_space(dataset.pixel_array, pi, rgb_photometric_interpretation)
        dataset.PixelData = rgb.tobytes()
        dataset.PhotometricInterpretation = rgb_photometric_interpretation
    except Exception as e:
        sys.stderr.write(f'Transcoding from {pi} to RGB failed. Reason: {e}\n')


def main():
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: dicom_decompress <input file> <output file>\n')
        exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    try:
        dataset = pydicom.dcmread(in_file, force=True)

        ts = dataset.file_meta.TransferSyntaxUID
        pi = dataset.PhotometricInterpretation

        if ts is not None:
            if ts in ts_decompress:
                decompress(dataset, ts)
                sys.stdout.write(f"Decompression successful from transfer syntax UID {ts}\n")
            elif ts in ts_skip:
                sys.stdout.write(f"Transfer syntax UID {ts} is uncompressed, skipping\n")
            else:
                sys.stdout.write(f"Transfer syntax UID {ts} not supported, skipping\n")

            if pi is not None:
                if pi in supported_photometric_interpretations:
                    transcode(dataset, pi)
                    sys.stdout.write(f"Transcoding successful from photometric interpretation {pi}\n")
            else:
                sys.stderr.write(f"Photometric interpretation missing\n")
        else:
            sys.stderr.write(f"Transfer syntax UID missing\n")

        pydicom.dcmwrite(out_file, dataset, write_like_original=False)

    except Exception as e:
        sys.stderr.write(f'Error in DICOM read/write: {e}\n')
        exit(1)


if __name__ == "__main__":
    main()
