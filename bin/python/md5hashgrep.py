#!/usr/bin/env python3
"""
Hash file grep looks for a line with a specific hash
"""

import sys
import hashlib

targetfile = sys.argv[1]

targethash = sys.argv[2]

linelist = [line.rstrip('\n') for line in open(targetfile)]

hashlist = list()

for line in linelist:
    LINEHASH = hashlib.md5(line.encode('utf-8')).hexdigest()
    hashlist.append(LINEHASH)

for md5hash in hashlist:
    print('Hash: {}'.format(md5hash))

if targethash in hashlist:
    print('MATCH: {}'.format(targethash))
