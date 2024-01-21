from iminuit import Minuit
import numpy as np
from scipy.stats import chi2

def fit(cost,*args,**kwargs):

    my_minuit = Minuit(cost,*args,**kwargs)
    my_minuit.migrad()
    my_minuit.hesse()
    return my_minuit

def likelihood(pdf,sample,*args,k=None,**kwargs):
    '''pdf(x,*args,**kwargs)'''
    return np.prod([ pdf(x,*args,**kwargs) for x in sample[:k]])

def loglikelihood(pdf,sample,*args,**kwargs):
    '''pdf(x,*args,**kwargs)'''
    return np.sum([np.log(pdf(x,*args,**kwargs)) for x in sample])

def p_value(q,doF):
    return chi2.cdf(q,doF)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from scipy.stats import norm
    from stats import *
    from iminuit.cost import*

    def pdf(x,a,b):
        return norm.pdf(x,a,b)

    def cdf(x,a,b):
        return norm.cdf(x,a,b)
    
    a,b = 1.5,.5
    data = toy_Gauss(a,b,2000).generate()

    # t = np.linspace(1,3,100)
    # ML = [likelihood(pdf,data,k=200,a=i,b=b) for i in t]
    bin_cont,bin_edges,p = plt.hist(data,sturges(data))

    plt.waitforbuttonpress()
    
    cst = UnbinnedNLL(data,pdf)
    # cst2 = BinnedNLL(bin_cont,bin_edges,cdf)

    f = fit(cst,a=0,b=1)
    f.interactive()
    plt.show()