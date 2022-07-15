#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# prints a list of existing modules

"""

Bootstrapping example of the python script, based on nouns and verbs

"""

from __future__ import print_function
import os
import sys
import csv
import json
import argparse

sys.dont_write_bytecode = True

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    PARSER.add_argument('--sc', '--sourcecreds', help="SourceCredentials")
    PARSER.add_argument('--sl', '--sourceenv', help="SourceEnvironment")
    PARSER.add_argument('--tc', '--targetcreds', help="TargetCredentials")
    PARSER.add_argument('--tl', '--targetenv', help="SourceEnvironment")
    PARSER.add_argument("action")
    PARSER.add_argument("target")
    PARSER.add_argument("adverb")
    ARGS = PARSER.parse_args()
    print(ARGS)

    print("Main before Import: got here...")

    import lib.nouns
    lib.nouns.describe()
    import lib.verbs
    lib.verbs.describe()
    import lib.creds
    lib.creds.describe()

    print("Main after Import: got here...")
