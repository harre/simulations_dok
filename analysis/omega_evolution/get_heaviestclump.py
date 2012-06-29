#!/usr/bin/python
import os
import sys
import numpy as np 

outlist = sys.argv[1]

outlistfile = open(outlist)
X = np.loadtxt(outlistfile)
max_per_col = X.max(axis=0)[2]
print max_per_col

