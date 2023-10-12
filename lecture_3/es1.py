import matplotlib.pyplot as plt
import numpy as np
from math import ceil,sqrt
import sys

f   = str('eventi_gauss.txt')


def file():
    '''opens the input file and outputs a list with the values as float'''
    sample = []
    with open(f,'r') as input_file:
        for i in input_file:
            sample.append(float(i))
    return sample

def xMin(sample):

    min=sample[0]
    for i in sample:
        if i<min:
            min = i
    return min


def xMax(sample):
    
    max=sample[0]
    for i in sample:
        if i>max:
            max = i
    return max

def positive(sample):
    '''prints the first 10 positive elements'''

    pos = []
    for i in sample:
        if i>=0:
            pos.append(i)
    return pos

def count(sample):
    '''returns the number of elements in the file'''
    return len(sample)

def mean(sample):
    '''first momentum'''
    return (sum(sample)/len(samples))

def variance(sample):
    s = 0
    m = mean(sample)
    for i in sample:
        s += ((i-m)*(i-m))
    return s/len(sample)

def stdDeviation(sample):
    return sqrt(variance(sample))

def sturges(sample):

    N = len(sample)
    return ceil(1+3.322*np.log(N))

def hist(sample):

    N_bins = sturges(sample)
    bin_edges = np.linspace(xMin(sample),xMax(sample),N_bins)

    fix,ax = plt.subplots(nrows= 1, ncols=1)
    ax.hist(sample,color = 'salmon',bins=bin_edges)
    plt.show()

def hist_N(sample,N:int):

    tmp = []
    for i in range(N):
        tmp.append(sample[i])
    hist(tmp)




if __name__ == '__main__':

    # N = int(input("Number of parameters:\t"))
    samples = file()
    print(variance(samples))
    hist(samples)
    # hist_N(samples,N)