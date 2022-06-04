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

import shutil
import os
import sys
import requests

MY_DIR = '/var/tmp/downloads'

os.makedirs(MY_DIR, exist_ok=True)

URL_NAME = 'https://logo.clearbit.com'

DNS_NAME = sys.argv[1]

IMG_FILE = os.path.join(MY_DIR, DNS_NAME)
ERR_FILE = os.path.join(MY_DIR, DNS_NAME + '.errors.txt' )

URL_NAME = 'https://logo.clearbit.com'

DNS_NAME = sys.argv[1]

response = requests.get(URL_NAME + '/' + DNS_NAME, stream=True)

status = response.status_code
print(status)

if status != 200:
    with open(ERR_FILE, 'w', encoding='utf8') as errors_file:
        errors_file.write(f'{status},{DNS_NAME},{URL_NAME},{IMG_FILE}')

if status == 200:
    with open(IMG_FILE, 'wb', encoding='utf8') as output_image:
        shutil.copyfileobj(response.raw, output_image)

del response
