import numpy as np
from scipy.stats import poisson,norm
import matplotlib.pyplot as plt
from scipy.integrate import quad
from math import pow,sin

def genericFunc(mean):

    f  = lambda x: norm.pdf(mean,x)
    f2 = lambda x: pow(x,3)+pow(x,2)-x
    f3 = lambda x: sin(x)/x

    return f3


def oneStd_x(mean,f):

    a=mean
    b=mean

    area = quad(func=f,a=-100,b=100)
    print(area[0])
    area1   =0
    area2   =0

    while area1 <= .34:
        area1 = quad(func=f,a=mean,b=b)[0]
        b+=.01

    while area2 <= .34:
        area2 = quad(func=f,a=a,b=mean)[0]
        a-=.01

    return a,b

if __name__== '__main__':
    
    fig,ax = plt.subplots(1,1)
    m = 3

    f = genericFunc(m)

    x = np.linspace(1,20,100)
    y = [f(i) for i in x]

    # print(oneStd_x(m,f))

    plt.axhline(0, color='gray')
    plt.axvline(0, color='gray')
    ax.plot(x,y)
    plt.show()