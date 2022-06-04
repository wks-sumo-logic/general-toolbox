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

import sys
import hashlib

targetfile = sys.argv[1]

targethash = sys.argv[2]

hashlist = []

with open(targetfile, 'r', encoding='utf8') as fileobject:
    for line in fileobject.readlines():
        line = line.rstrip()
        LINEHASH = hashlib.md5(line.encode('utf-8')).hexdigest()
        hashlist.append(LINEHASH)

for md5hash in hashlist:
    print(f'Hash: {md5hash}')

if targethash in hashlist:
    print(f'MATCH: {targethash}')
