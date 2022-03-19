#!/usr/bin/env python3
"""
Virus Total Scan example
"""

import os
import sys
import requests

URL = 'https://www.virustotal.com/vtapi/v2/file/scan'

apikey = sys.argv[1]
target = sys.argv[2]

params = {'apikey': apikey }

files = {'file': (target, open(os.path.abspath(target), 'rb'))}

response = requests.post(URL, files=files, params=params)

print(response.json())
