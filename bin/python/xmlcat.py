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
import pprint
import xmltojson

input_file = sys.argv[1]

with open(input_file, "r", encoding='utf8') as xml_file:
    xml_data = xml_file.read()
    json_data = xmltojson.parse(xml_data)

pprint.pprint(json_data)
