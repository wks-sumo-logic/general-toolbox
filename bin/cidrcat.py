#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
quick CIDR enumerator

Usage:
    $ cidrcat [addr] [mask]

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

    @name           cidrcat
    @version        0.8.00
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@gmail.com
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

__version__ = 1.00
__author__ = "Wayne Schmidt (wayne.kirk.schmidt@gmail.com)"

import sys
from netaddr import IPNetwork

sys.dont_write_bytecode = 1

NETBASE = sys.argv[1]
NETMASK = sys.argv[2]

for ipaddress in IPNetwork(NETBASE + '/' + NETMASK):
    print('%s' % ipaddress)
