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

with open(targetfile, "r", encoding='utf8') as fileobject:
    filecontents = fileobject.read()
    FILEHASH = hashlib.md5(filecontents.encode('utf-8')).hexdigest()
    print(f'{FILEHASH} {targetfile}')
