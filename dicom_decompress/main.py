import sys
import pydicom


def main():
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: dicom_decompress <input file> <output file>\n')
        exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    try:
        dataset = pydicom.dcmread(in_file, force=True)
        try:
            dataset.decompress()
        except:
            try:
                dataset.decompress('pylibjpeg')
            except Exception as e:
                sys.stdout.write(
                    f'Decompression attempted but failed, writing file as-is. Reason: {e}\n')
        pydicom.dcmwrite(out_file, dataset, write_like_original=False)
    except Exception as e:
        sys.stderr.write(f'Error in DICOM read/write: {e}\n')
        exit(1)


if __name__ == "__main__":
    main()
