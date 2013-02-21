#!/usr/bin/python

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math 
import os, sys, time, getopt, math, random
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp      
import matplotlib as mpl
import pyfits
from scipy import special
from matplotlib import rc
import os, sys, time, getopt, math, random
from matplotlib.ticker import MaxNLocator

inputfile = 'inputtemp'    
    
# load table (resp. array) from file - here 
# Rockstar Out-list 
Outlist = np.loadtxt(inputfile, delimiter=' ')

NumHalos = len(Outlist[:,0])

# Radius and masses we are interested in 
RadiusAroundCenter = 2.5 			# Mpc 
MinimalMassConsidered = 1E12 			# solar masses 
MaximalMassConsidered = 1E16 			# solar masses 
BoxSize = 20.0 					# Mpc

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

pmask=np.zeros(NumHalos)
pmask=pmask.astype(bool)
mask=np.zeros(NumHalos)
mask=mask.astype(bool)

for i in range(NumHalos):
	pmask[i] = (np.abs(Outlist[i, 8]-BoxSize/2.0) < RadiusAroundCenter and
		np.abs(Outlist[i, 9]-BoxSize/2.0) < RadiusAroundCenter and
		np.abs(Outlist[i, 10]-BoxSize/2.0) < RadiusAroundCenter )

for i in range(NumHalos):
	mask[i] = False
	if(MinimalMassConsidered < Outlist[i, 2] < MaximalMassConsidered):
		mask[i] = True & pmask[i]

#draw a vector
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


if len(Outlist[mask, 8]) > 0:
	    ax.scatter(Outlist[mask, 8]-BoxSize/2.0, Outlist[mask, 9]-BoxSize/2.0, Outlist[mask, 10]-BoxSize/2.0, c='#848484', s=35, edgecolors='none')
	    
	    for i in range(NumHalos): 
		    if(MinimalMassConsidered < Outlist[i, 2] < MaximalMassConsidered):
			    x = Outlist[i, 8]-BoxSize/2.0
			    dx = Outlist[i, 8]-BoxSize/2.0 + Outlist[i, 11]/5000.0
			    y = Outlist[i, 9]-BoxSize/2.0
			    dy = Outlist[i, 9]-BoxSize/2.0 + Outlist[i, 12]/5000.0
			    z = Outlist[i, 10]-BoxSize/2.0
			    dz = Outlist[i, 10]-BoxSize/2.0 + Outlist[i, 13]/5000.0
			    a = Arrow3D([x,dx],[y,dy],[z,dz], mutation_scale=20, lw=1, arrowstyle="-|>", color="k", alpha=0.5)
			    ax.add_artist(a)	    
	    #x[mask] = Outlist[mask, 8]-BoxSize/2.0
	    #dx[mask] = Outlist[mask, 8]-BoxSize/2.0 + Outlist[mask, 11]/1000.0
	    #y[mask] = Outlist[mask, 9]-BoxSize/2.0
	    #dy[mask] = Outlist[mask, 9]-BoxSize/2.0 + Outlist[mask, 12]/1000.0
	    #z[mask] = Outlist[mask, 10]-BoxSize/2.0
	    #dz[mask] = Outlist[mask, 10]-BoxSize/2.0 + Outlist[mask, 13]/1000.0
	    
	    #a = Arrow3D([x[mask],dx[mask]],[y[mask],dy[mask]],[z[mask],dz[mask]], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
	    #a = Arrow3D([Outlist[mask, 8]-BoxSize/2.0,Outlist[mask, 8]-BoxSize/2.0+Outlist[mask, 11]/1000.0], [Outlist[mask, 9]-BoxSize/2.0,Outlist[mask, 9]-BoxSize/2.0+Outlist[mask, 12]/1000.0], [ Outlist[mask, 10]-BoxSize/2.0, Outlist[mask, 10]-BoxSize/2.0+Outlist[mask, 13]/1000.0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
	    #ax.add_artist(a)

# Plot all Halos in List in a 3D Volume 		      
ax.scatter(Outlist[:,8]-BoxSize/2.0, Outlist[:,9]-BoxSize/2.0, Outlist[:,10]-BoxSize/2.0, c='#848484',s=2, edgecolors='none')
n=0
for i in range(NumHalos):
    if np.abs(Outlist[i, 8]-BoxSize/2.0) < 0.75 and np.abs(Outlist[i, 9]-BoxSize/2.0) < 0.75 and np.abs(Outlist[i, 10]-BoxSize/2.0) < 0.75 and MinimalMassConsidered < Outlist[i, 2] < MaximalMassConsidered: 
	  ax.text3D(Outlist[i, 8]-BoxSize/2.0, Outlist[i, 9]-BoxSize/2.0, Outlist[i, 10]-BoxSize/2.0,  np.str(Outlist[i,0]), size=6)
	  ax.text3D(Outlist[i, 8]-BoxSize/2.0, Outlist[i, 9]-BoxSize/2.0+0.15, Outlist[i, 10]-BoxSize/2.0+0.05,  'ang mom'+' '+np.str(Outlist[i,14]/1E12)+' '+np.str(Outlist[i,15]/1E12)+' '+np.str(Outlist[i,16]/1E12), size=3)
          ax.text3D(Outlist[i, 8]-BoxSize/2.0, Outlist[i, 9]-BoxSize/2.0-0.25, Outlist[i, 10]-BoxSize/2.0+0.05,  'vmax + vrms'+' '+np.str(Outlist[i,3])+' '+np.str(Outlist[i,4]), size=3)
          ax.text3D(Outlist[i, 8]-BoxSize/2.0-0.15, Outlist[i, 9]-BoxSize/2.0-0.20, Outlist[i, 10]-BoxSize/2.0+0.20,  'mass'+' '+np.str(Outlist[i,2]), size=3)
          n=n+1
          ax.text2D(0,1-n/25, 'coordinates of'+' '+np.str(Outlist[i,0])+': '+np.str(Outlist[i, 8])+' '+np.str(Outlist[i, 9])+' '+np.str(Outlist[i, 10]), size=5, transform=ax.transAxes)
	  ax.scatter(Outlist[i,8]-BoxSize/2.0, Outlist[i,9]-BoxSize/2.0, Outlist[i,10]-BoxSize/2.0, c='#DF0174',s=100, edgecolors='none')	

#pmask=np.zeros(NumHalos)
#pmask=pmask.astype(bool)
#mask=np.zeros(NumHalos) 
#mask=mask.astype(bool)

#for i in range(NumHalos):
	#pmask[i] = (np.abs(Outlist[i, 8]-BoxSize/2.0) < 1 and 
		#np.abs(Outlist[i, 9]-BoxSize/2.0) < 1 and
		#np.abs(Outlist[i, 10]-BoxSize/2.0) < 1 )

#mask [i]=True & pmask[i]
#ax.scatter(Outlist[mask, 8]-BoxSize/2.0, Outlist[mask, 9]-BoxSize/2.0, Outlist[mask, 10]-BoxSize/2.0, c='#2c89a0', s=30, edgecolors='none')

#labels = ['Outlist[i]'.format(i) for i in range(NumHalos)]
#for label, x, y in zip(labels,Outlist[mask, 8]-BoxSize/2.0, Outlist[mask, 9]-BoxSize/2.0, Outlist[mask, 10]-BoxSize/2.0):
    #plt.annotate(
        #label, 
        #xyz = (x, y, z), xytext = (-20, 20, 20),
        #textcoords = 'offset points', ha = 'right', va = 'bottom',
        #bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        #arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
        


coefs = (0.75, 0.75, 0.75)  # Coefficients in a0/c x**2 + a1/c y**2 + a2/c z**2 = 1 
# Radii corresponding to the coefficients:
rx, ry, rz = [1/np.sqrt(coef) for coef in coefs]

# Set of all spherical angles:
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

# Cartesian coordinates that correspond to the spherical angles:
# (this is the equation of an ellipsoid):
x = rx * np.outer(np.cos(u), np.sin(v))
y = ry * np.outer(np.sin(u), np.sin(v))
z = rz * np.outer(np.ones_like(u), np.cos(v))
ax.plot_wireframe(x, y, z,  color="#000000", rstride=8, cstride=8, alpha=0.1)
        
        
# Set the axis labels

ax.set_xlabel('Mpc (comoving)')
ax.set_ylabel('Mpc')
ax.set_zlabel('Mpc')
ax.set_title(inputfile)
ax.set_xlim3d(-RadiusAroundCenter/2.0,RadiusAroundCenter/2.0)	 
ax.set_ylim3d(-RadiusAroundCenter/2.0,RadiusAroundCenter/2.0)
ax.set_zlim3d(-RadiusAroundCenter/2.0,RadiusAroundCenter/2.0)
plt.savefig(inputfile+'Out'+'.'+'png',dpi=250,format='png')


