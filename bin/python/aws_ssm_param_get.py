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
import boto3

if len(sys.argv) > 1:
    CMD_INPUT = sys.argv[1]
else:
    sys.exit('Need to provide an argument please.')

print(f'INPUT: {CMD_INPUT}')

AWS_PARAM = 'UNSET'

"""
paramname = aws:ssm:us-east-1:sampleparam
"""

if "aws:ssm:" in CMD_INPUT:
    VENDOR, METHOD, REGION, TOKENS = CMD_INPUT.split(':')

    print(f'VENDOR: {VENDOR}')
    print(f'METHOD: {METHOD}')
    print(f'REGION: {REGION}')
    print(f'TOKENS: {TOKENS}')

    ssmobject = boto3.client(METHOD, region_name=REGION)

    ssmresponse = ssmobject.get_parameters(
        Names=[ TOKENS ],
        WithDecryption=True
    )

    print(f'{ssmresponse}')
    AWS_PARAM = ssmresponse['Parameters'][0]['Value']

print(f'AWSPARAM: {AWS_PARAM}')
