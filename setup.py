import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="dicom_decompress",
    version="0.0.1",
    description="Decompress jpeg/jpeg2000 DICOM files",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/exini/dicom-decompress",
    author="Karl Sjöstrand",
    author_email="karl.sjostrand@exini.com",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GPLv3 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["dicom_decompress"],
    include_package_data=False,
    python_requires='>=3.8',
    install_requires=[
        'numpy==1.20.1',
        'pydicom==2.1.2',
        'pylibjpeg==1.1.1',
        'pylibjpeg-libjpeg==1.1.0',
        'pylibjpeg-openjpeg==1.0.1',
        'wheel==0.35.1'
    ],
    entry_points={
        'console_scripts': ['dicom-decompress=dicom_decompress.main:main']
    },
)
