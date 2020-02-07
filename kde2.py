# %matplotib inline
# %pylab inline
from sklearn.neighbors.kde import KernelDensity
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import argrelextrema
import subprocess
import math

def k():
    op = subprocess.check_output(['awk', '$1~/cpu[0-9]/{usage=($2+$4)*100/($2+$4+$5); print usage}', '/proc/stat'])
    ar = op.split('\n')[0:-1]
    ar = list(map(float, ar))
    # ar.extend([4.0,30.0,24.0])
    print(ar)
    X = np.array(ar).reshape(-1,1)
    kde = KernelDensity(kernel = 'gaussian', bandwidth=3).fit(X)
    s = np.linspace(0,50)
    e = kde.score_samples(s.reshape(-1,1))
    # plt(s,e)
    mi, ma = argrelextrema(e, np.less)[0], argrelextrema(e, np.greater)[0]
    print ("Minima:", s[mi])
    print ("Maxima:", s[ma])
    if(len(mi) < 2):
        ar.sort()
        mi = ar[0:len(ar)/2]
        ma = ar[len(ar)/2:]
        print(mi, ma)
        mi = list(map(int,mi))
        ma = list(map(int,ma))
    else:
        print (X[X < mi[0]], X[(X >= mi[0]) * (X <= mi[1])], X[X >= mi[1]]) 
    plt.plot(s,e)
    plt.show()
    plt.plot(s[:mi[0]+1], e[:mi[0]+1], 'r',
    s[mi[0]:mi[1]+1], e[mi[0]:mi[1]+1], 'g',
    s[mi[1]:], e[mi[1]:], 'b',
    s[ma], e[ma], 'go',
    s[mi], e[mi], 'ro')
    plt.show()
    print(plot(s,e))

if __name__ == "__main__":
    k()
    input()
