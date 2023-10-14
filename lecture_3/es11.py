import matplotlib.pyplot as plt
from scipy.stats import poisson
import numpy as np


'''Write a Python program to draw a Poisson distribution 
    for several values of its mean, overlapped'''

def poisson_(ax,mu,n):

    x = np.arange(0,n,.1)
    ax.plot(x,poisson.pmf(x,mu))


if __name__ == '__main__':

    fig,ax = plt.subplots(nrows=1,ncols=1)

    poisson_(ax,1,100)
    poisson_(ax,3,100)
    poisson_(ax,25,100)
    poisson_(ax,35,100)
    poisson_(ax,45,100)

    plt.show()