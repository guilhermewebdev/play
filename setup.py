#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='Play',
    version='0.1',
    description='Play video in terminal',
    author='Guilherme Isaías',
    author_email='guilherme@guilhermeweb.dev',
    url='https://github.com/guilhermewebdev/play',
    install_requires=[
        'opencv-python',
        'Pillow',
    ],
    packages=['lib', 'lib.cli', 'lib.entities', 'lib.controllers'],
    entry_points={
        'console_scripts': ['play=lib.cli:play']
    }
)