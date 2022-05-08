#!/usr/bin/env python3

from distutils.core import setup
import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='play-video',
    version='1.0.4',
    description='Play video on terminal',
    author='Guilherme Isaías',
    author_email='guilherme@guilhermeweb.dev',
    url='https://github.com/guilhermewebdev/play',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description_file='README.md',
    license='GNU General Public License v3.0',
    platforms=['Linux', 'MacOS', 'Windows'],
    install_requires=[
        'opencv-python',
        'Pillow',
    ],
    packages=setuptools.find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': ['play=lib.cli:play']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Multimedia :: Video :: Display",
        "Framework :: Pytest",
    ],
    python_requires='>=3.7',
)