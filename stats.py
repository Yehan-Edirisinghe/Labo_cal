import numpy as np
import matplotlib.pyplot as plt
from random import random
import matplotlib.pyplot as plt

class graph():

    def __init__(self,sample):
        
        self.sample = sample
        fig,ax = plt.subplots(1,1)

        Nbins = int(len(self.sample)/10)
        
        ax.hist(self.sample,bins=Nbins)

    def show(self):

        
        plt.show()

class Normal_stats:

    def __init__(self,sample):

        self.sample = sample

    def mean(self,sample = None):
        
        if sample != None:
            return np.average(sample)
        
        return np.average(self.sample)
    
    def variance(self):

        m = self.mean()
        sum = 0

        for i in range(len(self.sample)):
            sum += (self.sample[i]-m)**2

        return sum/len(self.sample)
    
    def standard_deviation(self):

        return np.sqrt(self.variance)
    
    def skewness(self):

        return 0
    
    def kurtosis(self):
        
        return 0
    
    def stats(self):

        m = np.average(self.sample)
        v = self.variance()
        s = self.skewness()
        k = self.kurtosis()

        return m,v,s,k
    
class toy_Gauss:

    def __init__(self,N_max,N_toys) -> None:
        
        self.sample = self.Gaussian_Distribution(N_max,N_toys)


    def toy(self,N_max):
        
        list = [random() for i in range(N_max)]

        return np.average(list)

    def Gaussian_Distribution(self,N_max,N_toys):

        toys = [self.toy(N_max) for i in range(N_toys)]

        return toys
    

class toy_Exp:

    def __init__(self,t_o,t_Max,N=100) -> None:
        
        self.t_o = t_o
        self.t_Max = t_Max
        self.N = N

    def single_event(self):
        '''return time interval between two random events, that behave like an exponential'''

        return -self.t_o*np.log(1-random())

    def exponential(self,N):
        '''returns a toy exponential sample'''

        return [self.single_event() for i in range(N)]


class toy_Poiss:

    def __init__(self,t_o,t_Max,N):

        self.t_o = t_o
        self.t_Max = t_Max
        self.N = N
        
        self.exp = toy_Exp(self.t_o,self.t_Max)

    
    def singleEventCounter(self):

        t = 0
        counter = 0
        
        while(t < self.t_Max):

            counter += 1
            t += self.exp.single_event()

        return counter

    def Poisson_Distr(self):

        return [self.singleEventCounter() for i in range(self.N)]
    


    
        
        



if __name__== '__main__':
    

    #GAUSSIAN TEST

    # N = 1000
    # M = 1000
    # toy = toy_Gauss(N,M)
    # sample = toy.sample
    # stats = Normal_stats(sample)

    #EXPONENTIAL TEST

    # toy = toy_Exp(5,100)
    # sample = toy.exponential(1000)

    # POISSON TEST

    # to = 1
    # tmax = 100
    # N = 1000
    # toy = toy_Poiss(to,tmax,N)
    # sample = toy.Poisson_Distr()




    grph = graph(sample)
    grph.show()
    # m,v,s,k = stats.stats()

    

