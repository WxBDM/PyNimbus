#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='PyNimbus',
    version='0.0.3',
    long_description=README,
    long_description_content_type="text/markdown",
    description='A Python package to organize National Weather Service product data.',
    url='https://github.com/WxBDM/PyNimbus',
    author='Brandon Molyneaux',
    author_email='bdmolyne@gmail.com',
    license='BSD 3-clause "New" or "Revised License"',
    packages=['pynimbus'],
    install_requires = ['pandas>=0.23.4'],
    zip_safe=True,
    classifiers=[
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Natural Language :: English",
    ],
    keywords = "meteorology weather",
    project_urls = {
        'Documentation' : 'https://pynimbus.readthedocs.io/en/latest/',
        'GitHub Repo' : 'https://github.com/WxBDM/PyNimbus',
        'Issues' : 'https://github.com/WxBDM/PyNimbus/issues'
    }
)