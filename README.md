# dicom-decompress

A command-line utility for decompressing DICOM files with compressed pixel data

## Usage

* **To build**: `python setup.py sdist bdist_wheel` *(requires python3 + wheel package)*
* **To install**: `pip install --force-reinstall dist/dicom-decompress-x.y.z-py3-none-any.whl`, *(x.y.z is version, see setup.py)*
* **To run**: Run the terminal command `dicom-decompress <input file> <output file>`.
    * To decompress multiple files in-place run e.g.
      ```bash
      find . -name "*.dcm" -exec dicom-decompress {} {} \;
      ```
  
