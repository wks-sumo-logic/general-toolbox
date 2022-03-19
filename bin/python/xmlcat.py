#!/usr/bin/env python3
"""
XML file pretty print
"""

import sys
import pprint
import xmltojson

input_file = sys.argv[1]

with open(input_file, "r") as xml_file:
    xml_data = xml_file.read()
    json_data = xmltojson.parse(xml_data)

pprint.pprint(json_data)
