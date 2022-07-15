#!/usr/bin/env python3

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


headers = ['timeslice', 'totalnumber']

csvfile = sys.argv[1]

df = pd.read_csv(csvfile, names=headers)

df.set_index('timeslice').plot()

### plt.show()

data = df['totalnumber']

peaks, _ = find_peaks(data, height=20)

plt.plot(data)

plt.plot(peaks, data[peaks], "x")

plt.show()

