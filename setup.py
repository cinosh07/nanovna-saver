#  NanoVNASaver - a python program to view and export Touchstone data from a NanoVNA
#  Copyright (C) 2019.  Rune B. Broberg
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from NanoVNASaver.about import version
from os.path import join, dirname, abspath

ROOT_DIRECTORY = dirname(abspath(__file__))
SKINS_DIR = join(ROOT_DIRECTORY, "skins\\")
if sys.version_info < (3, 7):
    print("You need at least Python 3.7 for this application!")
    if sys.version_info[0] < 3:
        print("try running with python3 {}".format(" ".join(sys.argv)))
    sys.exit(1)

try:
    print("Root directory is: " + ROOT_DIRECTORY)
    from setuptools import setup, find_packages
except ImportError:
    print("Could not find setuptools")
    print("Try installing them with pip install setuptools")
    sys.exit(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='NanoVNASaver',
    url='https://github.com/mihtjel/nanovna-saver',
    version=version,
    author='Rune B. Broberg',
    author_email='',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='LICENSE.txt',
    entry_points={
        'console_scripts': [
            'NanoVNASaver = NanoVNASaver.__main__:main'
        ],
    },
    install_requires=[
        'pyserial',
        'PyQt5==5.11.2',
        'numpy',
        'qtpy'
    ],
    package_data={'NanoVNASaver': ['skins/*.css']},
    data_files=[('skins', [SKINS_DIR+"dark-colored.css", SKINS_DIR+"light-colored.css", SKINS_DIR+"dark-monochrome.css", SKINS_DIR+"light-monochrome.css"])]
)
