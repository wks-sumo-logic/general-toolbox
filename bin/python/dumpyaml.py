#!/usr/bin/env python3
"""
Simple cat file for YAML into a python data structure
"""

import json
import sys
import pprint
import yaml

input_file = sys.argv[1]

with open(input_file, "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file.read())

pprint.pprint(json.dumps(yaml_data))
