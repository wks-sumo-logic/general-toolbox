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

import os
import sys
import pandas

totalframe = pandas.DataFrame()

sourcedir = sys.argv[1]

outputfile = sys.argv[2]

filelist = os.listdir(sourcedir)

for file in filelist:
    dataframe = pandas.read_csv(os.path.join(sourcedir, file))
    totalframe = pandas.concat((dataframe, totalframe), axis=0)

totalframe.to_csv(outputfile, index=False)
