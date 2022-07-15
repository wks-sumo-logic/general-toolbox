#!/usr/bin/env python3

import datetime
import dateutil
import dateutil.tz
import time

datestamp = datetime.datetime.strptime("2011-01-21 02:37:21", "%Y-%m-%d %H:%M:%S")

utcdate = datestamp.replace(tzinfo=datetime.timezone.utc)
print('utcdate: {}'.format(utcdate.strftime("%Y-%m-%d %H:%M:%S %Z")))

jstdate = utcdate.astimezone()
print('jstdate: {}'.format(jstdate.strftime("%Y-%m-%d %H:%M:%S %Z")))

nowdate = datetime.datetime.now().astimezone()
nowzone = datetime.datetime.now().astimezone().tzinfo
print('nowdate: {}'.format(nowdate.strftime("%Y-%m-%d %H:%M:%S %Z")))

newdate = time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime())
print(newdate)

utc_zone = dateutil.tz.tzutc()
local_zone = dateutil.tz.tzlocal()

newdate = nowdate.astimezone(utc_zone)
print(newdate.strftime("%Y-%m-%d %H:%M:%S %Z"))
