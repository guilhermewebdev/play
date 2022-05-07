#!/usr/bin/env python3

from distutils.core import setup
from importlib.metadata import entry_points
import pathlib
import pkg_resources

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name='Play',
    version='0.1',
    description='Play video in terminal',
    author='Guilherme Isaías',
    author_email='guilherme@guilhermeweb.dev',
    url='https://www.python.org/sigs/distutils-sig/',
    install_requires=install_requires,
    packages=['src', 'src.cli', 'src.entities', 'src.controllers'],
    entry_points={
        'console_scripts': ['play=src.cli:play']
    }
)