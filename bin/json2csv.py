#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Explanation: converts json files to csv format

Usage:
   $ python  json2csv [ options ]

Style:
   Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

    @name           json2csv
    @version        1.0.0
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@gmail.com
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

__version__ = '1.0.0'
__author__ = "Wayne Schmidt (wayne.kirk.schmidt@gmail.com)"

import argparse
import os
import pathlib
import sys
import pandas

sys.dont_write_bytecode = 1

PARSER = argparse.ArgumentParser(description="""

This is designed as a sample converter of json files to csv format.
It will keep the source and the destination file

""")

PARSER.add_argument('-s', metavar='<srcfile>', dest='srcfile', help='input file to cleanup')

ARGS = PARSER.parse_args()

def main():
    """
    This is a driver to convert json files into CSV format
    """
    json2csv(os.path.abspath(ARGS.srcfile))

def json2csv(srcfile):
    """
    Opens up the source file and destination file, and ensures utf8 encoding
    """

    srcpathobj = pathlib.Path(os.path.abspath(srcfile))
    dstfile = srcpathobj.with_suffix('.csv')

    with open(srcfile, encoding='utf-8-sig') as srcfileobj:
        datafile = pandas.read_json(srcfileobj)

    datafile.to_csv(dstfile, encoding='utf-8', index=False)

if __name__ == '__main__':
    main()
