#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Explanation:

Simple CSV file validator

Usage:
    $ python3 validatecsvfile.py <filename>

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

    @name           validatecsvfile.py
    @version        1.0.0
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@gmail.com
    @license-name   Apache 2.0
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

import os
import sys
import csv
from csvvalidator import CSVValidator, write_problems

FIELD_NAMES = ''

csvfile = os.path.abspath(sys.argv[1])

with open (csvfile, "r", encoding='utf8') as csvobject:
    csvdata = csv.reader(csvobject, delimiter=",")
    FIELD_NAMES = next(csvdata)

validator = CSVValidator(FIELD_NAMES)

validator.add_header_check('EX1', 'bad header')

validator.add_record_length_check('EX2', 'unexpected record length')

print(f'### Starting Validation of: {csvfile}')

with open (csvfile, "r", encoding='utf8') as csvobject:
    csvdata = csv.reader(csvobject, delimiter=",")
    csvproblems = validator.validate(csvdata)
    write_problems(csvproblems, sys.stdout, summarize=True, limit=0)

print(f'### Completed Validation of: {csvfile}')
