import numpy as np


def ML(data,func,*args):
    
    return np.prod([func(i,args[0],args[1]) for i in data])

def loglikelihood(data,func,*args):

    return np.sum( np.log( [func(i,args[0],args[1]) for i in data] ))

def max_sez_aurea(sample,func,t,prec=.001):

    r = (-1+np.sqrt(5))/2  #golden ratio

    xmin = min(t)
    xmax = max(t)

    while abs(xmax-xmin) > prec:

        a = xmin +     r* abs(xmax-xmin)
        b = xmin + (1-r)* abs(xmax-xmin)
        
        if func(sample,b) < func(sample,a):
            xmin = b
        else: 
            xmax = a

    return xmin,func(sample,xmin)

if __name__ == '__main__':

    import files as f
    from scipy.stats import norm
    import matplotlib.pyplot as plt

    dati = f.read_file('lecture_12/dati2.txt')


    t = np.linspace(-10,10,50)

    # mean_graph = [ ML(dati[:300],norm.pdf,i,1) for i in t ]
    
    # plt.plot(t,mean_graph)
    # plt.show()

    mean_graph = [ loglikelihood(dati[:10000],norm.pdf,3,i) for i in t ]
    
    plt.plot(t,mean_graph)
    plt.show()