#!/usr/bin/env python3
"""
Calculate a MD5 hash for a file
"""

import sys
import hashlib

targetfile = sys.argv[1]

with open(targetfile, "r") as fileobject:
    filecontents = fileobject.read()
    FILEHASH = hashlib.md5(filecontents.encode('utf-8')).hexdigest()
    print('{} {}'.format(FILEHASH, targetfile))
