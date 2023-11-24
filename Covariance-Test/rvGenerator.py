import sys
sys.path.append('/home/peppo/Documents/Labo_cal/')
from Libraries.files import file
from Libraries.stats import stdDeviation

import numpy as np
import matplotlib.pyplot as plt


def noCorrelation(N):

    x = np.random.uniform(0,1,N)
    y = np.random.uniform(0,1,N)

    # y = np.array([np.sin(i*(5+np.random.uniform(0,.25))) for i in x])

    return x,y

def linearCorrelation(N):

    x = np.random.normal(size=N)
    y = np.array([(i*(5+np.random.uniform(0,.35))) for i in x])

    return x,y

def covariance(x,y):
    
    v = x,y

    cov = np.empty((2,2))

    for l in range(2):
        for k in range(2):
            
            cov[l,k] = stdDeviation(v[l])*stdDeviation(v[k])

    r = (cov[0,1]*cov[1,0])/(cov[1,1]*cov[0,0])

    return cov,r

if __name__ == '__main__':

    fig,ax = plt.subplots(1,1)

    x,y = noCorrelation(2000)
    # x,y = linearCorrelation(2000)

    ax.scatter(x,y)

    cov,r = covariance(x,y)

    print(cov,'\n',r)

    plt.show()