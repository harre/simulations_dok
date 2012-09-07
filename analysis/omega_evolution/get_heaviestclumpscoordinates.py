#!/usr/bin/python
import os
import sys
import numpy as np 

# start from snapshot number
outlist = sys.argv[1]


outlistfile = open(outlist)
X = np.loadtxt(outlistfile)
max_per_col = X.max(axis=0)[2]

lineofmvirmax = np.array(X[np.where(X==max_per_col)[0]])

clumpx = lineofmvirmax[0][8]
clumpy = lineofmvirmax[0][9] 
clumpz = lineofmvirmax[0][10]

print lineofmvirmax[0][8], lineofmvirmax[0][9], lineofmvirmax[0][10]