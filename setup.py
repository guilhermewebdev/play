#!/usr/bin/env python3

from distutils.core import setup
from importlib.metadata import entry_points
from pathlib import Path
import pkg_resources

requirements_path = Path(__file__).parent / "requirements.txt"

with requirements_path.open() as requirements_txt:
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
    url='https://github.com/guilhermewebdev/play',
    install_requires=install_requires,
    packages=['lib', 'lib.cli', 'lib.entities', 'lib.controllers'],
    entry_points={
        'console_scripts': ['play=lib.cli:play']
    }
)