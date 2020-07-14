#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan .
@Bryan .

Made with love by Bryan .

==================================
DESC:
    Will return the parsed CSV file given as
a python dict or JSON. This is meant to be
read and has functions that you may use in
other projects.
==================================

VERSION: Final

"""

import sys  # In order to be able to use sys.stdin or sys.stdout

import argparse  # The main big boy of this program

from pathlib2 import Path

from CSVParser import parseCSV


parser = argparse.ArgumentParser(description="""
    To convert CSV files into either a JSON or a n-dimensional list.
    Output is defaulted to stdout but may be
    changed to a file if option -f or --file is defined

    Dependancies:
     - NumPy | python3 -m pip install numpy
     - Pathlib2 | python3 -m pip install pathlib2

    """, prog='csv2other')
parser.add_argument(
    'i',
    type=str,
    nargs='?',
    default='sys.stdin',
    help='The csv file.')
parser.add_argument(
    '-f', '--output-file', '-o', '--output',
    type=argparse.FileType('w'),
    default=sys.stdout,
    nargs='*',
    help='The file to write the converted csv to.')
parser.add_argument(
    '-t', '-type', '--output-type',
    default='dict',
    choices=[
        'dict',
        'json',
        "list",
        "numpy",
        "array",
        "matrix",
        "np.array",
        "np.ndarray",
        "numpy.array",
        "numpy.ndarray"],
    nargs='?',
    help="For changing the output type. Can be json or an array")

args = parser.parse_args()

if Path(
    str(args.i)).expanduser().exists() and Path(
    str(
        args.i)).expanduser().is_file():
    zeInFile = str(Path(str(args.i)).expanduser().read_text())
else:
    raise BaseException("Error: %s is not a valid path to a file \
or %s doesn't exist." % (args.i, args.i))


print()


try:
    zeOutFile = args.output_file[0]
except TypeError:
    zeOutFile = args.output_file
print(
    parseCSV(zeInFile, args.output_type),
    file=zeOutFile)
