import numpy as np
from random import random

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
   
# CLASSES #

class toy_Gauss:

    def __init__(self,mean=0,sigma=1,N=1000,n=100) -> None:
        
        self.mean = mean
        self.sigma = sigma
        self.sample = self.normal(N,n)
        self.bins = self.sturges(self.sample)
        # self.stats = stat(self.sample)

    def sturges(self,sample):
        '''returns the surges function applied to the sample length'''

        N = len(sample)
        return int(np.ceil(1+3.322*np.log(N)))

    def normal(self,N,n):
        '''toy normal distribution'''

        delta = np.sqrt(3*n)*self.sigma
        a = np.empty(N)

        for i in range(N):

            a[i] = np.average([ np.random.uniform(self.mean-delta , self.mean+delta) for j in range(n) ])
    
        return a  

class toy_Exp:

    def __init__(self,t_o=1,N=1000):
        
        self.t_o = t_o
        self.N = N
        self.bins = int(np.ceil(1+3.322*np.log(N)))
        self.sample = self.exponential()
        self.stats = stat(self.sample)

    def sgl_evt(self):
        '''return number that behave like an exponential '''

        return -self.t_o*np.log(1-random())

    def exponential(self):
        '''returns a toy exponential sample'''

        return [self.sgl_evt() for i in range(self.N)]
    
class toy_Poiss:

    def __init__(self,t_o,t_Max,N):

        self.t_o    = t_o
        self.t_Max  = t_Max
        self.N      = N

        self.bins = int(np.ceil(1+3.322*np.log(N)))
        self.sample = self.Poisson_Distr()
        self.stats = stat(self.sample)

    def singleEventCounter(self):

        t = 0
        counter = 0
        
        while(t < self.t_Max):

            counter += 1

            t += -self.t_o*np.log(1-random())

        return counter

    def Poisson_Distr(self):

        return [self.singleEventCounter() for i in range(self.N)]
    
    def stats2(self):

        m = np.average(self.sample)
        v = m
        s = 1/np.sqrt(m)
        k = 1/m

        return m,v,s,k
    
#
#   MINIMUM AND ZEROS
#
    
def max_sez_aurea(func,xmin,xmax,prec=.001):

    r = (-1+np.sqrt(5))/2  #golden ratio
    

    while abs(xmax-xmin) > prec:

        a = xmin +     r* abs(xmax-xmin)
        b = xmin + (1-r)* abs(xmax-xmin)
        
        if func(b) < func(a):
            xmin = b
        else: 
            xmax = a

    return xmin,func(xmin)

if __name__== '__main__':
    
    import matplotlib.pyplot as plt
    
    #########################################
    #GAUSSIAN TEST
    #########################################

    data = toy_Gauss(mean=2,sigma=2)

    print("mean:\t",data.stats[0],"\n",
          "variance:\t",data.stats[1],"\n",
          "skewness:\t",data.stats[2],"\n",
          "kurtosis:\t",data.stats[3],"\n")
    
    plt.hist(data.sample,bins=data.bins)
    plt.show()

    #########################################
    #EXPONENTIAL TEST
    #########################################

    # to = 4
    # N = 1000
    # data = toy_Exp(to,N)

    # print("mean:\t",data.stats[0],"\n",
    #       "variance:\t",data.stats[1],"\n",
    #       "skewness:\t",data.stats[2],"\n",
    #       "kurtosis:\t",data.stats[3],"\n")

    # plt.hist(data.sample,bins=data.bins)
    # plt.show()

    #########################################
    # POISSON TEST
    #########################################

    # to = 1
    # tmax = 100
    # N = 200

    # data = toy_Poiss(to,tmax,N)

    # print("mean:\t",data.stats[0],"\n",
    #       "variance:\t",data.stats[1],"\n",
    #       "skewness:\t",data.stats[2],"\n",
    #       "kurtosis:\t",data.stats[3],"\n")
    # plt.hist(data.sample)
    # plt.show()