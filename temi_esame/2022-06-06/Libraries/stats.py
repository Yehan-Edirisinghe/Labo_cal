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

    def __init__(self,t_o=1,N=1000):
        
        self.t_o = t_o
        self.N = N

    def generate(self):
        
        self.sample = self.exp_distr()
        self.bins = sturges(self.sample)
        self.stats = stat(self.sample)
        return self.sample

    def exp(self,t_0):
        '''returns number that behave like an exponential '''

        return -t_0*np.log(1-np.random.uniform())

    def exp_distr(self):
        '''returns a toy exponential sample'''

        return [self.exp(self.t_o) for i in range(self.N)]
    
class toy_Poiss:

    def __init__(self,t_o,t_Max,N):

        self.t_o    = t_o
        self.t_Max  = t_Max
        self.N      = N

    def generate(self):
        self.sample = self.Poisson_Distr()
        self.bins = sturges(self.sample)
        self.stats = stat(self.sample)
        return self.sample

    def singleEventCounter(self):

        t = 0
        counter = 0
        
        while(t < self.t_Max):
            counter += 1
            t += -self.t_o*np.log(1-np.random.uniform())

        return counter

    def Poisson_Distr(self):

        return [self.singleEventCounter() for i in range(self.N)]
    
if __name__ == '__main__':

    from scipy.stats import kurtosis as kk,skew
    import matplotlib.pyplot as plt

    data = toy_Poiss(2,10,1000).generate()

    var = variance(data)
    stnd = std(data)
    skw = skewness(data)
    kurt = kurtosis(data)

    print(var, np.var(data))
    print(stnd, np.std(data))
    print(skw, skew(data))
    print(kurt, kk(data))
    plt.hist(data,bins=sturges(data))
    plt.show()