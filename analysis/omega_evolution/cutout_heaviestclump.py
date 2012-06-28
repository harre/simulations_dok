#!/usr/bin/python
import os
import sys
import numpy as np 

# start from snapshot number
startnum = 0
endnum = int(sys.argv[1])

inputpath  = sys.argv[2]
outputpath = sys.argv[2]
outlist = sys.argv[3]

outlistfile = open(outlist)
X = np.loadtxt(outlistfile)
max_per_col = X.max(axis=0)[2]
print '>> Maximal Mvir in this out_list file:', max_per_col

lineofmvirmax = np.array(X[np.where(X==max_per_col)[0]])

print '>> Coordinates of this clump', lineofmvirmax[0][8], lineofmvirmax[0][9], lineofmvirmax[0][10]

clumpx = lineofmvirmax[0][8]
clumpy = lineofmvirmax[0][9] 
clumpz = lineofmvirmax[0][10]
snapname='snapshot_'

for i in range(startnum,endnum+1,10):
    #print i
    inputName = inputpath+snapname+str(i).zfill(3)
    outputName = outputpath+'cutout/'+'snapshot_cut_'+str(i).zfill(3)
    print ' Converting '+inputName+' to '+ outputName
    print ' ---------------------------------------------------'
    os.system('/home/harre/code/analysis/gadget_tools/cutout '+inputName+' '+outputName+' '+str(clumpx)+' '+str(clumpy)+' '+str(clumpz))


