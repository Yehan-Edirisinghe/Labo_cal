import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from math import ceil,sqrt
import sys

f   = str('eventi_gauss.txt')


def file(name:str):
    '''opens the input file and outputs a list with the values as float'''
    sample = []
    with open(name,'r') as input_file:
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
    return (sum(sample)/len(sample))

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

def gaussian(sample):
    
    m   = xMin(sample)
    M   = xMax(sample)
    mea =mean(sample)
    sigma = stdDeviation(sample)

    x = np.arange(m,M,0.1)
    y = []
    for i in x:
        y.append(norm.pdf(i,mea,sigma))
    fix,ax = plt.subplots(nrows= 1, ncols=1)
    ax.plot(x,y)
    plt.show()

def hist(sample):

    m = mean(sample)
    o = stdDeviation(sample)

    N_bins = sturges(sample)
    bin_edges = np.linspace(xMin(sample),xMax(sample),N_bins)

    fix,ax = plt.subplots(nrows= 1, ncols=1)
    ax.hist(sample,color = 'salmon',bins=bin_edges)
    # mean line
    vertical_limit = ax.get_ylim()
    ax.plot([m,m],vertical_limit,color='blue')
    # # std deviation line
    ax.plot([m+o,m+o],vertical_limit,color='red')
    ax.plot([m-o,m-o],vertical_limit,color='red')

    plt.show()


def hist_N(sample,N:int):

    tmp = []
    for i in range(N):
        tmp.append(sample[i])
    hist(tmp)

class data:
    
    def __init__(self,fileName):
        self.sample = file(fileName)
        self.mean = mean(self.sample)
        self.variance = variance(self.sample)
        self.stdDeviation = stdDeviation(self.sample)
        self.len = len(self.sample)

    def plot(self):
        hist(self.sample)

    def plot_N(self,N):
        hist_N(self.sample,N)
    
    def gauss(self):
        gaussian(self.sample)

if __name__ == '__main__':

    # N = int(input("Number of parameters:\t"))
    # samples = file(f)
    # print(variance(samples))
    # hist(samples)
    # hist_N(samples,N)

    a = data(f)
    a.plot()
    a.gauss()

    # print(a.mean)