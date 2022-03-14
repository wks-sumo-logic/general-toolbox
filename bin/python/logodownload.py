#!/usr/bin/env python3
"""
Download Logos from:

https://logo.clearbit.com/<company_domain_name>
"""

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
    with open(ERR_FILE, 'w') as errors_file:
        errors_file.write('{},{},{},{}'.format(status,DNS_NAME,URL_NAME,IMG_FILE))

if status == 200:
    with open(IMG_FILE, 'wb') as output_image:
        shutil.copyfileobj(response.raw, output_image)

del response
