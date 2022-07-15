#!/usr/bin/env python3

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import pandas as pd

csvfile = sys.argv[1]
data = pd.read_csv(csvfile, sep=',',header=None, index_col =0)
data.plot(kind='bar')
plt.show()
