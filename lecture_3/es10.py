import es
import numpy as np
from math import factorial as fact,pow
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.stats import binom


'''Write a Python program to draw a binomial distribution and its cumulative function'''

def binomial(n,p):
    
    x = list(range(n))
    y =[]    
    for k in range(n):
        y.append(binom.pmf(k,n,p))
    return x,y

def cdfBinomial(n,p):

    x = list(range(n))
    y = []
    for k in range(n):
        y.append(binom.cdf(k,n,p))
    return x,y


if __name__ == '__main__':

    fig,ax = plt.subplots(nrows=1,ncols=2)
    
    n,p = 100,.4

    bin = binomial(n,p)
    cum = cdfBinomial(n,p)

    ax[0].plot(bin[0],bin[1])
    ax[1].plot(cum[0],cum[1])

    plt.show()