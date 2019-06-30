#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='exif2pandas',
    version='1.0',
    description="Generate sql database with exif data.",
    author="Visgean",
    author_email='visgean@gmail.com',
    url='https://github.com/visgean/exif2pandas',
    packages=[
        'exif2pandas',
    ],
    package_dir={'exif2pandas': 'exif2pandas'},
    license="MIT",
    keywords='exif sql',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'exifread',
        'pandas'

    ],
    entry_points={
        'console_scripts': [
            'exif2pandas = exif2pandas.main:main'
        ]
    },
)