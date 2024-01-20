from iminuit import Minuit
import numpy as np
 
def fit(cost,*args,**kwargs):

    my_minuit = Minuit(cost,*args,**kwargs)
    my_minuit.migrad()
    my_minuit.hesse()
    return my_minuit

def likelihood(pdf,sample,k=None,*args,**kwargs):
    '''pdf(x,*args,**kwargs)'''
    return np.prod([ pdf(x,*args,**kwargs) for x in sample[:k]])

def loglikelihood(pdf,sample,*args,**kwargs):
    '''pdf(x,*args,**kwargs)'''
    return np.sum([np.log(pdf(x,*args,**kwargs)) for x in sample])

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from scipy.stats import norm
    from stats import toy_Gauss
    from iminuit.cost import LeastSquares,UnbinnedNLL,BinnedNLL

    def pdf(x,a,b):
        return norm.pdf(x,a,b)

    a,b = 1.5,.5
    data = toy_Gauss(a,b,2000).generate()

    t = np.linspace(1,3,100)
    ML = [likelihood(pdf,data,k=200,a=i,b=b) for i in t]

    cst = UnbinnedNLL(data,pdf)
    f = fit(cst,a=0,b=1)
    print(f)
    # plt.hist(data,bins=100)
    # plt.plot(t,ML)
    # plt.show()