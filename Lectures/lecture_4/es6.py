'''Implement a pseudo-random number generator that uses 
the inverse function method to generate events distributed according to an exponential probability distribution'''

import random
from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np

def uniformDistribution(N):

    y=[]
    for i in range(N):
        y.append(random.random())
    return y

def inv_Func(N):

    x = uniformDistribution(N)
    
    
    return expon.pdf(x)



if __name__ == '__main__':

    N = 100000


    sample = inv_Func(N)

    fig,ax = plt.subplots(1,1)
    ax.hist(sample,color='salmon',bins=100)
    plt.show()