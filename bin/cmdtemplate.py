#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Explanation:

This is a sample command line python script

Usage:
    $ python  template [ options ]

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

    @name           rfslsync
    @version        1.0.0
    @author-name    Wayne Schmidt
    @author-email   wschmidt@sumologic.com
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

__version__ = '1.0.0'
__author__ = "Wayne Schmidt (wschmidt@sumologic.com)"

import argparse
import configparser
import datetime
import os
import sys

sys.dont_write_bytecode = 1

PARSER = argparse.ArgumentParser(description="""

This script connects Recorded Future to SumoLogic in the following manner.
Retrieves the information from Recorded Future in CSV format
Pushes the files to Sumologic hosted Web collector.

""")

PARSER.add_argument('-k', metavar='<key>', dest='key', help='set key')
PARSER.add_argument('-d', metavar='<dir>', dest='dir', help='set directory')
PARSER.add_argument('-c', metavar='<cfg>', dest='cfg', help='set config file')
PARSER.add_argument('-v', '--verbose', help='verbose', action="store_true")

ARGS = PARSER.parse_args()
CURRENT = datetime.datetime.now()
DSTAMP = CURRENT.strftime("%Y%m%d")
TSTAMP = CURRENT.strftime("%H%M%S")
LSTAMP = DSTAMP + '.' + TSTAMP
BASEDIR = os.path.abspath((os.path.join(os.environ['HOME'])))

if ARGS.cfg:
    CFGFILE = os.path.abspath(ARGS.cfg)
    CONFIG = configparser.ConfigParser()
    CONFIG.read(CFGFILE)

if ARGS.key:
    os.environ['APIKEY'] = ARGS.key

if ARGS.dir:
    BASEDIR = os.path.abspath((os.path.join(ARGS.dir)))
try:
    APIKEY = os.environ['APIKEY']
except KeyError as myerror:
    print('ISSUE!!! Environment Variable Not Set :: {} '.format(myerror.args[0]))
    sys.exit()

def main():
    """
    This is the template for the main logic of the script
    """
    print('APIKEY :: {} '.format(APIKEY))
    print('BASEDIR :: {} '.format(BASEDIR))
    print('LOGSTAMP :: {} '.format(LSTAMP))

if __name__ == '__main__':
    main()
