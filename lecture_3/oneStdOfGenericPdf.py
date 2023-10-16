import numpy as np
from scipy.stats import poisson,norm

from scipy.integrate import quad

def genericF(mean):
    f = lambda x: poisson(mu=mean,k=x)

def oneStd_x(mean,f):

    a=mean
    b=mean

    area=0
    area2 = 0

    while area<.32:
        area = quad(func=f,a=mean,b=a)[0]
        a+=.001
    while area2<.32:
        area2 = quad(func=f,a=b,b=mean)[0]
        b-=.001
    return a,b

if __name__=='__main__':
    
    x = np.linspace(norm.ppf(0.01),norm.ppf(0.99), 100)
    f = lambda x : norm.pdf(x,2)
    norm_fix = norm (0, 1)
    print(norm_fix)
    print(oneStd_x(mean=0,f=norm_fix.pdf))