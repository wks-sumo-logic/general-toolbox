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
import requests

URL = 'https://www.virustotal.com/vtapi/v2/file/scan'

apikey = sys.argv[1]
target = sys.argv[2]

params = {'apikey': apikey }

targetpath = os.path.abspath(target)

with open (targetpath, 'rb') as fileobject:
    filecontents = fileobject.read()
    files = {'file': filecontents}

response = requests.post(URL, files=files, params=params)

print(response.json())
