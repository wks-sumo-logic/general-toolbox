#!/usr/bin/env python3
"""
Clump output from CSV files into Pandas dataframe
"""

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
