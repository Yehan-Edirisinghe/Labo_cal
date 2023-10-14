import es
import numpy as np
from math import factorial as fact,pow
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.stats import binom


'''Write a Python program to draw a binomial distribution and its cumulative function'''

def binomial(k,n,p):
    
    x = list(range(n))
    y =[]
    
        # y.append(   (fact(n)/(fact(k)*fact(n-k)))*pow(p,k)*pow((1-p),(n-k)) )
    y=binom.pmf(k,n,p)
    return x,y

def cdfBinomial(x_,y_):

    x = x_
    y = []
    for i in range(len(x)):
        y.append(quad())
    return x,y

fig,ax = plt.subplots(nrows=1,ncols=1)
x,y = binomial(10,200,.15)
ax.plot(x,y)
plt.show()