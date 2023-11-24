import sys
sys.path.append('/home/peppo/Documents/Labo_cal/')
from Libraries.files import file
from Libraries.stats import stdDeviation

import numpy as np
import matplotlib.pyplot as plt


def noCorrelation(N):

    x = np.random.uniform(0,np.pi,N)
    # y = np.random.uniform(0,1,N)

    y = np.array([np.sin(i*(5+np.random.uniform(0,.25))) for i in x])

    return x,y

def linearCorrelation(N):

    x = np.random.normal(size=N)

    y = np.array([(i*(5+np.random.uniform(0,.35))) for i in x])

    return x,y

def cov(x,y):
    
    sum = 0
    m = np.average(x)
    n = np.average(y)

    for i in range(len(x)):
        
        sum += (x[i]-m)*(y[i]-n)

    return sum/len(x)

def covMatrix(x,y):

    mat = np.empty((2,2))

    mat[0,0] = cov(x,x)
    mat[0,1] = cov(x,y)
    mat[1,0] = cov(y,x)
    mat[1,1] = cov(y,y)

    r = mat[1,0]*mat[0,1]/(mat[0,0]*mat[1,1])

    return mat,r**2

if __name__ == '__main__':

    fig,ax = plt.subplots(1,1)

    # x,y = noCorrelation(2000)
    x,y = linearCorrelation(2000)

    ax.scatter(x,y)

    cov,r = covMatrix(x,y)

    print(cov,'\n\n','Correlation:',r)

    plt.show()