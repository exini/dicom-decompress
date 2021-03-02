# dicom-decompress

A command-line utility for decompressing DICOM files with compressed pixel data

## Usage

* **To build**: `python setup.py sdist bdist_wheel` *(requires python3, wheel package must be installed (pip install wheel))*
* **To install**: `pip install --force-reinstall --user dist/dicom-decompress-x.y.z-py3-none-any.whl`, where x.y.z is version (look in output of build)
* **To run**: Run the terminal command `dicom-decompress <input file> <output file>`.
  *On Windows the executable file is placed in \<user_dir\>\\AppData\\Roaming\Python\Python3x\Scripts, i.e. probably not on PATH*
  
