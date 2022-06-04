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

import os
import sys
import json
from benedict import benedict

JSON_FILE = os.path.abspath(sys.argv[1])
with open (JSON_FILE, "r", encoding='utf8') as fileobject:
    myjson = json.load(fileobject)
    mydict = benedict(myjson)
    keypaths = mydict.keypaths()
    for keypath in keypaths:
        print(f'path: {keypath}')
