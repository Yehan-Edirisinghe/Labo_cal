import matplotlib.pyplot as plt
from scipy.stats import poisson
import numpy as np
from es import gaussian


'''Write a Python program to draw a Poisson distribution 
    for several values of its mean, overlapped'''

def poisson_(ax,mu,n):

    m,v,s,k = poisson.stats(mu,moments='mvsk')
    x = np.arange(0,n,.1)
    lab = "mean:"+str(round(m,2))+ "  skew: "+str(round(s,2)) + " Kurt" +str(round(k,2))
    ax.plot(x,poisson.pmf(x,mu),label = lab)



if __name__ == '__main__':

    fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(7,6))
    
    n = 1000

    poisson_(ax,10,n)
    poisson_(ax,20,n)
    poisson_(ax,50,n)
    poisson_(ax,200,n)
    poisson_(ax,500,n)

    ax.legend()
    
    plt.show()