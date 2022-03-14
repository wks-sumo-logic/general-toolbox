#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Explanation: removes comments from json files

Usage:
   $ python  jsoncstrip [ options ]

Style:
   Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

    @name           jsoncstrip
    @version        1.0.0
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@gmail.com
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

__version__ = '1.0.0'
__author__ = "Wayne Schmidt (wayne.kirk.schmidt@gmail.com)"

import argparse
import json
import os
import re
import sys

sys.dont_write_bytecode = 1

PARSER = argparse.ArgumentParser(description="""

This will read in a JSON file and strip out comments

""")

PARSER.add_argument('-s', metavar='<srcs>', nargs='*', dest='srcs', help='files to cleanup')

ARGS = PARSER.parse_args()

def remove_comments(json_like):
    """
    This removes commentds by a multiline regular expression
    """
    comments_re = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    def replacer(match):
        matched_group = match.group(0)
        if matched_group[0] == '/':
            return ""
        return matched_group
    return comments_re.sub(replacer, json_like)

def remove_trailing_commas(json_like):
    """
    This is a cleanup function, also multiline regular expression
    """
    trailing_object_commas_re = re.compile(
        r'(,)\s*}(?=([^"\\]*(\\.|"([^"\\]*\\.)*[^"\\]*"))*[^"]*$)')
    trailing_array_commas_re = re.compile(
        r'(,)\s*\](?=([^"\\]*(\\.|"([^"\\]*\\.)*[^"\\]*"))*[^"]*$)')
    # Fix objects {} first
    objects_fixed = trailing_object_commas_re.sub("}", json_like)
    # Now fix arrays/lists [] and return the result
    return trailing_array_commas_re.sub("]", objects_fixed)

if __name__ == "__main__":
    for file in ARGS.srcs:
        STAGE0_JSON = ""
        filepath = os.path.abspath(file)
        with open(filepath, 'r') as file:
            STAGE0_JSON = file.read()
            STAGE1_JSON = remove_comments(STAGE0_JSON)
            STAGE2_JSON = remove_trailing_commas(STAGE1_JSON)
            FINAL_JSON = json.loads(STAGE2_JSON)
            print(json.dumps(FINAL_JSON, indent=4))
