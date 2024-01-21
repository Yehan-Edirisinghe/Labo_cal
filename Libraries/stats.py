import numpy as np
from random import random

# BASIC FUNCTIONS #

def mean(sample):
    sum = 0
    for i in sample:
        sum +=i
    return sum/len(sample)

def variance(sample):
    m = np.average(sample)
    v = 0
    for i in sample:
        v += (i - m)**2
    
    return v/((len(sample)))

def std(sample):
    return np.sqrt(variance(sample))

def skewness(sample):

    m = mean(sample)
    sk = 0
    for i in sample:
        sk += (i - m)**3

    return sk/((len(sample)-1)*(std(sample)**3))

def kurtosis(sample):

    m = np.average(sample)
    k = 0

    for i in sample:
        k += (i - m)**4

    return k/((len(sample)-1)*std(sample)**4) -3

def stat(sample):
        '''functions that returns mvsk moments of data pdf'''

        m = mean(sample)
        v = std(sample)
        s = skewness(sample)
        k = kurtosis(sample)

        return m,v,s,k

def sturges(sample):
    '''returns the surges function applied to the sample length'''

    N = len(sample)
    return int(np.ceil(1+3.322*np.log(N)))

def rand_uniform(xmin,xmax,N):
    return abs(xmax-xmin)*random() +xmin

# CLASSES #

class toy_Gauss:

    def __init__(self,mean=0,sigma=1,N=1000,n=100) -> None:
        
        self.mean = mean
        self.sigma = sigma
        self.N = N
        self.n = n
        
    def generate(self):

        self.sample = self.normal_distr(self.N,self.n)
        self.bins = sturges(self.sample)
        self.stats = stat(self.sample)

        return self.sample
    
    def normal(self,mean,sigma,n=1000):

        delta = np.sqrt(3*n)*sigma

        return np.average([ np.random.uniform(mean-delta , mean+delta) for j in range(n) ])

    def normal_distr(self,N,n):
        '''toy normal distribution'''
    
        return [self.normal(self.mean,self.sigma,n) for i in range(N)]

class toy_Exp:

    def __init__(self,l=1,N=1000):
        
        self.l = l
        self.N = N

    def generate(self):
        
        self.sample = self.exp_distr()
        self.bins = sturges(self.sample)
        self.stats = stat(self.sample)
        return self.sample

    def exp(self,l):
        '''returns number that behave like an exponential'''

        return -l*np.log(1-np.random.uniform())

    def exp_distr(self):
        '''returns a toy exponential sample'''

        return [self.exp(self.l) for i in range(self.N)]
    
class toy_Poiss:

    def __init__(self,lambda_,t0=1,N=1000):
        '''lamba: mean of distribution\n
            t0 coefficient of expon'''

        self.lambda_  = lambda_
        self.N      = N
        self.t0    = t0

        if lambda_ < t0:
            raise Exception("lambda_ has to be grater than to")
    
    def generate(self):
        self.sample = self.Poisson_Distr()
        self.bins = sturges(self.sample)
        self.stats = stat(self.sample)
        return self.sample
    
    def rand_poisson(self,lambda_,t0=1):

        t, counter = 0,0

        while(t < lambda_):
            counter += 1
            t += -t0*np.log(1-np.random.uniform())
        
        return counter-1

    def Poisson_Distr(self):
        return [self.rand_poisson(self.lambda_,self.t0) for i in range(self.N)]
    
if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from fit import*
    from iminuit.cost import *
    from scipy.stats import expon

    def f(x,a,b):
        return expon.pdf(x,a,b)
    
    N = 1000
    x = toy_Exp(N=N).generate()
    x2 = np.random.standard_exponential(N)
    bin_cont, bin_edges, pol = plt.hist(x)
    plt.close()

    err = 0.3*np.ones(len(bin_cont))
    cst = LeastSquares(bin_edges[1:],bin_cont,err,f)

    f = fit(cst,a=0,b=1)
    f.interactive()
    print(f)
    plt.show()