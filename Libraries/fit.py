from iminuit import Minuit
import numpy as np
import scipy.stats as sc

def fit(cost,*args,interactive=False,**kwargs):

    my_minuit = Minuit(cost,*args,**kwargs)
    my_minuit.migrad()
    my_minuit.hesse()
    if interactive == True:
        my_minuit.interactive()
    return my_minuit

def likelihood(pdf,sample,*args,k=None,**kwargs):
    '''pdf(x,*args,**kwargs)'''
    return np.prod([ pdf(x,*args,**kwargs) for x in sample[:k]])

def loglikelihood(pdf,sample,*args,**kwargs):
    '''pdf(x,*args,**kwargs)'''
    return np.sum([np.log(pdf(x,*args,**kwargs)) for x in sample])

def p_value(q,doF):
    return sc.chi2.sf(q,doF)

def chi2_corr(chi2,N_K):
    a = N_K/chi2
    chi2_cor = chi2/a
    return chi2_cor


if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from scipy.stats import expon
    from stats import*
    from iminuit.cost import*

    data = toy_Exp(l=3).generate()
    b_c, b_e, b_p = plt.hist(data,density=True,bins=100)
    y_e = .01*np.ones(len(b_c))

    def pdf(x,a,b):
        return b*expon.pdf(x,0,a)
    
    cst = LeastSquares(b_e[1:],b_c,y_e,pdf)
    m = Minuit(cst,a=1,b=1)
    m.migrad()
    m.hesse()
    # print(m)
    print(m.hesse())
    m.interactive()
    print(p_value(m.fval,m.ndof))
    # plt.show()