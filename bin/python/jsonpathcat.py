#!/usr/bin/env python3
"""
Print out all paths in JSON file
Note: If the keys contains a "." this will cause an error
"""

import os
import sys
import json
from benedict import benedict

JSON_FILE = os.path.abspath(sys.argv[1])
with open (JSON_FILE, "r") as fileobject:
    myjson = json.load(fileobject)
    mydict = benedict(myjson)
    keypaths = mydict.keypaths()
    for keypath in keypaths:
        print('path: {}'.format(keypath))
