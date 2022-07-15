#!/usr/bin/env python3

import datetime
import dateutil
import dateutil.tz
import time
import sys


string="2017-08-14T06:49:20Z"
string = ( string.replace('T', ' ').replace('Z', '') )
print(string)

### string = "2011-01-21 02:37:21"
datestamp = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

utcdate = datestamp.replace(tzinfo=datetime.timezone.utc)
print('utcdate: {}'.format(utcdate.strftime("%Y-%m-%d %H:%M:%S %Z")))

jstdate = utcdate.astimezone()
print('jstdate: {}'.format(jstdate.strftime("%Y-%m-%d %H:%M:%S %Z")))
