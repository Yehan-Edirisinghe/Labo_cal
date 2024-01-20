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

    def __init__(self,t0,t1,N=1000):

        self.t_o    = t0
        self.t_Max  = t1
        self.N      = N

        # if t_Max < t_o:
        #     raise Exception("tmax has to be grater than to")
    
    def generate(self):
        self.sample = self.Poisson_Distr()
        self.bins = sturges(self.sample)
        self.stats = stat(self.sample)
        return self.sample
    
    def rnd_poiss(self,media):
        x = 0
        p = np.exp(-media)
        s = p
        u = random()

        while u > s:
            x += 1
            p *= media / x
            s += p

        return x
    
    def singleEventCounter(self):

        t, counter = 0,0
        
        while(t < self.t_Max):
            counter += 1
            t += np.random.exponential(self.t_o)
            # t += -self.t_Max*np.log(1-np.random.uniform())
        
        return t/counter

    def Poisson_Distr(self):

        return [self.singleEventCounter() for i in range(self.N)]
    
if __name__ == '__main__':

    from scipy.stats import kurtosis as kk,skew
    import matplotlib.pyplot as plt

    data = toy_Poiss(3,4,1000).generate()
    # data = [np.random.standard_exponential() for i in range(200)]
    print(np.mean(data))

    plt.hist(data,bins=sturges(data))
    plt.show()