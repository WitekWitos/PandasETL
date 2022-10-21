#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
import pathlib



from setuptools import find_packages, setup 

# Package meta-data.
NAME = 'classes'
DESCRIPTION = 'My short description for my project.'
URL = 'https://github.com/WitekWitos/PandasETL'
EMAIL = 'witold.piwowarski.pollub@gmail.com'
AUTHOR = 'Witold Piwowarski'
REQUIRES_PYTHON = '>=3.10.0'
VERSION = '0.0.1'

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
]


# Where the magic happens:
setup(
    name=NAME,
    version='0.0.1',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license='Custom'
    )