import numpy as np

# BASIC FUNCTIONS #

def mean(sample):
    return np.average(sample)

def variance(sample):
    return np.var(sample)

def stdDeviation(sample):
    return np.std(sample)

def skewness(sample):

    m = np.average(sample)
    sk = 0
    for i in sample:

        sk += (i - m)**3
    
    return sk/((len(sample)-1)*(np.std(sample)**3))

def kurtosis(sample):

    m = np.average(sample)
    k = 0

    for i in sample:
        k += (i - m)**4
    
    return k/((len(sample)-1)*np.std(sample)**4)

def stat(sample):
        '''functions that returns mvsk moments of data pdf'''

        m = np.average(sample)
        v = np.var(sample)
        s = skewness(sample)
        k = kurtosis(sample)

        return m,v,s,k

def sturges(sample):
    '''returns the surges function applied to the sample length'''

    N = len(sample)
    return int(np.ceil(1+3.322*np.log(N)))

# CLASSES #

# Gaussian


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

    def singleEventCounter(self):

        t = 0
        counter = 0
        
        while(t < self.t_Max):
            counter += 1
            t += -self.t_o*np.log(1-np.random.uniform())

        return counter

    def Poisson_Distr(self):

        return [self.singleEventCounter() for i in range(self.N)]