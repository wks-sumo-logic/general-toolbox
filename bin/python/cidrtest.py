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
import ipaddress
import argparse
sys.dont_write_bytecode = 1

PARSER = argparse.ArgumentParser(description="""

cidrtest calculates if a address is in a specific cidr block.
currently expects an ipv4 address and can be adapted to other checks

""")

PARSER.add_argument("-c", metavar='<cidr>', dest='cidrblock', help="specify a target CIDR block")
PARSER.add_argument("-i", metavar='<addr>', dest='ipaddress', help="specify a target IP address")

ARGS = PARSER.parse_args()

try:
    TARGETCIDR = ARGS.cidrblock
    TARGETADDR = ARGS.ipaddress
except KeyError as myerror:
    print(f'Environment Variable Not Set :: {myerror.args[0]}')

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
        print(f'CIDR: {TARGETCIDR} contains Address: {TARGETADDR}')
    else:
        print(f'CIDR: {TARGETCIDR} excludes Address: {TARGETADDR}')

if __name__ == '__main__':
    main()
