#!/usr/bin/python3
import os
import sys
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import os
import regex as re

plt.ion()

def plotspec(fname, pol, lim=None):
    fig, ax= plt.subplots();
    have_blindscan = False
    try:
        x=np.loadtxt(fname)
        f=x[:,0]
        spec = x[:,1]
        ax.plot(f, spec, label="spectrum (dB)")

        tps=np.loadtxt(fname.replace('spectrum', 'blindscan'))
        f1= tps[:,0]/1000
        spec1 = tps[:,0]*0+-70000
        ax.plot( f1, spec1,  '+', label="Found TPs")
        have_blindscan = True
    except:
        pass
    if have_blindscan:
        title='Blindscan result - {fname}'
    else:
        title='Spectrum - {fname}'
    plt.title(title.format(pol=pol, fname=fname));
    plt.legend()
    if lim is not None:
        ax.set_xlim(lim)
    return


d='/tmp'

rx = re.compile('(spectrum)([HV]).dat$')
def find_data(d='/tmp/'):
    ret=[]
    for root, dirs, files in os.walk(d):
      for file in files:
          res = re.match(rx, file)
          if res is not None:
              fname = os.path.join(root, file)
              print(fname)
              ret.append((fname, res.group(2)))
    return ret

files=find_data(d)



for file, pol in files:
    plotspec(file, pol=pol)
