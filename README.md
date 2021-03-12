# dicom-decompress

A command-line utility for decompressing DICOM files with compressed pixel data. Optionally, ff photometric 
interpretation is one of `YBR_FULL`, `YBR_FULL_422`, `PALETTE COLOR` pixel data will be transcoded to `RBG`.


## Installation

```bash
pip install dicom-decompress
```

This will install the terminal command `dicom-decompress` in your environment.

To decompress a single file run

```bash
dicom-decompress in.dcm out.dcm
```

where `in.dcm` is the file to decompress and `out.dcm` is the decompressed target file. To attempt transcoding for non
monochrome or rgb images add the `--transcode` flag:

```bash
dicom-decompress --transcode in.dcm out.dcm
```

To decompress multiple files in-place run e.g.

```bash
find . -name "*.dcm" -exec echo {} \; -exec dicom-decompress --transcode {} {} \;
```

### Dependencies

* [numpy](https://pypi.org/project/numpy/)
* [pydicom](https://pypi.org/project/pydicom/)

## Development

* **To build**: `python setup.py sdist bdist_wheel` *(requires python3 + wheel package)*
* **To install**: `pip install --force-reinstall dist/dicom_decompress-x.y.z-py3-none-any.whl`, *(x.y.z is version, see
  setup.py)*
* **To publish**
  * Install twine: `pip install twine`
  * Build package (cf. above)
  * Make sure it passes the twine check: `twine check dist/*`
  * Publish: `twine upload dist/*`
