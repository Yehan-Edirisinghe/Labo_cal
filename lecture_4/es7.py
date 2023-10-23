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


def randGauss(M,N):

    
    gaussian = []

    for i in range(M):
        t = uniformDistribution(N)
        m = avarage(t)
        gaussian.append(norm.pdf(m))

    return gaussian




if __name__ == '__main__':

    N = 1000
    M = 10000

    # print(uniformDistribution(N))

    sample = randGauss(N,M)

    fig,ax = plt.subplots(1,1)
    ax.hist(sample,color='salmon',bins=20)
    plt.show()