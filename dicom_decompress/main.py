import sys
import pydicom


def main():
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: dicom_decompress <input file> <output file>')
        exit(1)

    try:
        dataset = pydicom.dcmread(sys.argv[1], force=True)
        try:
            dataset.decompress()
        except:
            try:
                dataset.decompress('pylibjpeg')
            except Exception as e:
                sys.stderr.write(f'Decompression not possible: {e}')
                exit(1)
        pydicom.dcmwrite(sys.argv[2], dataset, write_like_original=False)
    except Exception as e:
        sys.stderr.write(f'Error in DICOM read/write: {e}')
        exit(1)


if __name__ == "__main__":
    main()
