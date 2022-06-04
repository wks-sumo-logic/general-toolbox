#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
    @version        1.0.00
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@gmail.com
    @license-name   APACHE 2.0
    @license-url    http://www.apache.org/licenses/LICENSE-2.0
"""
__version__ = 1.00
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
