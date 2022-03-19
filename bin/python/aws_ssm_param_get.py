#!/usr/bin/env python3

"""
Sample Driver for AWS SSM parameter retrieval
"""

import sys
import pprint
import boto3

if len(sys.argv) > 1:
    CMD_INPUT = sys.argv[1]
else:
    sys.exit('Need to provide an argument please.')

print('INPUT: {}'.format(CMD_INPUT))

AWS_PARAM = 'UNSET'

"""
paramname = aws:ssm:us-east-1:sampleparam
"""

if "aws:ssm:" in CMD_INPUT:
    VENDOR, METHOD, REGION, TOKENS = CMD_INPUT.split(':')

    print('VENDOR: {}'.format(VENDOR))
    print('METHOD: {}'.format(METHOD))
    print('REGION: {}'.format(REGION))
    print('TOKENS: {}'.format(TOKENS))

    ssmobject = boto3.client(METHOD, region_name=REGION)

    ssmresponse = ssmobject.get_parameters(
        Names=[ TOKENS ],
        WithDecryption=True
    )

    pprint.pprint(ssmresponse)
    AWS_PARAM = ssmresponse['Parameters'][0]['Value']

print('AWSPARAM: {}'.format(AWS_PARAM))
