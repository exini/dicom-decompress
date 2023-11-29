import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="dicom-decompress",
    version="1.0.1",
    description="Minimal command-line tool for decompressing DICOM files with compressed pixel data.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/exini/dicom-decompress",
    author="Karl Sjöstrand",
    author_email="karl.sjostrand@exini.com",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["dicom_decompress"],
    include_package_data=False,
    install_requires=[
        'numpy==1.21.6',
        'pydicom==2.4.3'
    ],
    entry_points={
        'console_scripts': ['dicom-decompress=dicom_decompress.main:main']
    },
)
