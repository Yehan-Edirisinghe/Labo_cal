import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from math import ceil,sqrt


def file(name:str):
    '''opens the input file and outputs a list with the values as float'''

    sample = []
    with open(name,'r') as input_file:
        for i in input_file:
            sample.append(float(i))
    return sample

def xMin(sample):
    '''returns the min value in sample spaace'''

    min=sample[0]
    for i in sample:
        if i<min:
            min = i
    return min


def xMax(sample):
    '''returns the max value in sample space'''

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
    '''returns the variance of the sample space'''

    s = 0
    m = mean(sample)
    for i in sample:
        s += ((i-m)*(i-m))
    return s/len(sample)

def stdDeviation(sample):
    return sqrt(variance(sample))

def sturges(sample):
    '''returns the surges function applied to the sample length'''

    N = len(sample)
    return ceil(1+3.322*np.log(N))

def gaussian(sample,ax):
    '''plot the gaussian of the sample space'''

    m   = xMin(sample)
    M   = xMax(sample)
    mea =mean(sample)
    sigma = stdDeviation(sample)

    x = np.arange(m,M,0.1)
    y = []
    for i in x:
        y.append(norm.pdf(i,mea,sigma))
    ax.plot(x,y)

def cumulativeDF(sample,me,std,ax):
    '''plots the cumulative df of the sample space'''

    m   = xMin(sample)
    M   = xMax(sample)

    x = np.arange(m,M,0.1)
    y = []
    for i in x:
        y.append(norm.cdf(i,me,std))
    ax.plot(x,y)


def hist(sample,ax):
    '''draws a histogram of the sample space'''
    m = mean(sample)
    o = stdDeviation(sample)

    N_bins = sturges(sample)
    bin_edges = np.linspace(xMin(sample),xMax(sample),N_bins)

    ax.hist(sample,color = 'salmon',bins=bin_edges)
    # mean line
    vertical_limit = ax.get_ylim()
    ax.plot([m,m],vertical_limit,color='blue')
    # # std deviation line
    ax.plot([m+o,m+o],vertical_limit,color='red')
    ax.plot([m-o,m-o],vertical_limit,color='red')

def hist_N(sample,N:int,ax):
    '''hist with the first n elements of sample space'''
    tmp = []
    for i in range(N):
        tmp.append(sample[i])
    hist(tmp)

class data:
    '''object that rappresenta the sample space data with pdf and plotting devices'''
    def __init__(self,fileName):
        
        self.sample = file(fileName)
        self.mean = mean(self.sample)
        self.variance = variance(self.sample)
        self.stdDeviation = stdDeviation(self.sample)
        self.len = len(self.sample)
        fig,ax = plt.subplots(nrows= 1, ncols=1,label=fileName)
        self.ax = ax
        

    def hist(self,ax=None):
        if ax!= None:
            
            hist(self.sample,ax)
        else:
            hist(self.sample,self.ax)


    def hist_N(self,N,ax=None):
        if ax!=None:
            hist_N(self.sample,ax)
        else:
            hist_N(self.sample,self.ax)

    def gauss(self,ax=None):
        if ax!=None:
            gaussian(self.sample,ax)

        else:
            gaussian(self.sample,self.ax)


    def cdf(self,ax=None):
        if ax!=None:
            cumulativeDF(self.sample,self.mean,self.stdDeviation,ax)
        else:
            cumulativeDF(self.sample,self.mean,self.stdDeviation,self.ax)
        


if __name__ == '__main__':
    
    f   = str('eventi_gauss.txt')
    a = data(f)
    fig1,ax1=plt.subplots(nrows=1,ncols=2)
    a.hist(ax=ax1[0])
    a.gauss(ax=ax1[1])
    plt.show()

