#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exaplanation: cidrtest - is an IP is contained within a CIDR block

Usage:
   $ python  cidrtest [ options ]

Style:
   Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

    @name           cidrtest
    @version        1.00
    @author-name    Wayne Schmidt
    @author-email   wschmidt@sumologic.com
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

__version__ = '1.0.0'
__author__ = "Wayne Schmidt (wschmidt@sumologic.com)"

import sys
import ipaddress
import argparse
sys.dont_write_bytecode = 1

PARSER = argparse.ArgumentParser(description="""

cidrinout calculates if a address is in a specific cidr block.
currently expects an ipv4 address and can be adapted to other checks

""")

PARSER.add_argument("-c", metavar='<cidr>', dest='cidrblock', help="specify a target CIDR block")
PARSER.add_argument("-i", metavar='<addr>', dest='ipaddress', help="specify a target IP address")

ARGS = PARSER.parse_args()

try:
    TARGETCIDR = ARGS.cidrblock
    TARGETADDR = ARGS.ipaddress
except KeyError as myerror:
    print('Environment Variable Not Set :: {} '.format(myerror.args[0]))

def main():
    """
    perform the enumeration of the network and calculate the ip address
    """
    network = ipaddress.IPv4Network(TARGETCIDR)
    firstip, finalip = network[0], network[-1]

    firstint = int(ipaddress.IPv4Address(firstip))
    finalint = int(ipaddress.IPv4Address(finalip))
    targetint = int(ipaddress.IPv4Address(TARGETADDR))
    if firstint <= targetint <= finalint:
        print('CIDR: {} contains Address: {}'.format(TARGETCIDR, TARGETADDR))
    else:
        print('CIDR: {} excludes Address: {}'.format(TARGETCIDR, TARGETADDR))

if __name__ == '__main__':
    main()
