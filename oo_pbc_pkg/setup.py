"""

Package setup file using setuptools.

Project: Python Boot Camp
Author: OO
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oo_pbc_pkg",
    version="0.0.1",
    author="OO",
    author_email="oloosvald@gmail.com",
    description="Python boot camp package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/oliso/PythonBoot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
