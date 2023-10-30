'''Implement a pseudo-random number generator that uses the central limit theorem 
    method to generate events distributed according to a Gaussian probability distribution'''


from random import random
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np


def uniformDistribution(N):

    y=[]

    for i in range(N):
        y.append(random())
    
    return y

def avarage(l):

    sum = 0

    for i in l:
        sum += i
    return sum/len(l)


def randGauss(M):

    means=[]
    
    for i in range(N):
    
    	t = uniformDistribution(M)
    	means.append(avarage(t))
    
    return means



if __name__ == '__main__':

    N = 1000

    #sample = (uniformDistribution(N))

    sample = randGauss(N)
   
    
    fig,ax = plt.subplots(1,1)
    ax.hist(sample,color='salmon')
    plt.show()