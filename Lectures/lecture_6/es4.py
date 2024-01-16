from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

'''Determine the minimum of the function g(x) = x2 + 7.3x + 4 
    using the golden ratio search method in the interval (-10, 10).'''

r = (-1+sqrt(5))/2

def f(x):
    return -((x-1)**2)

def g(x):
    return x**2 + (7.3*x) +4

def minimum(func,xmin,xmax,precision=.0001, x2=None,x3=None):
    
    if(sqrt((xmax-xmin)**2) < precision):
        return xmin
    
    if (x2 != None):
        x2 = x2
        x3 = xmin + (1-r)*(xmax-xmin)

    elif x3 != None:
        x2 = xmin +     r*(xmax-xmin)
        x3 = x3
    else:
        x2 = xmin +     r*(xmax-xmin)
        x3 = xmin + (1-r)*(xmax-xmin)
    
    if(func(x3) > func(x2)):
        return minimum(func,x3,xmax,precision,x3=x2)
    else:
        return minimum(func,xmin,x2,precision,x2=x3)

def maximum(func,xmin,xmax,precision):
    
    d = abs(xmax-xmin)

    if(d < precision):
        return xmin
    
    x2 = xmin +     r* d
    x3 = xmin + (1-r)* d
    
    if(func(x3) < func(x2)):
        return maximum(func,x3,xmax,precision)
    else:
        return maximum(func,xmin,x2,precision)

def graph(func,xm,xM):

    x = np.arange(xm,xM,0.05)
    y = [func(i) for i in x]
    fig,ax = plt.subplots(1,1)
    ax.plot(x,y)
    return ax

if __name__ == '__main__':

    m = minimum(g,-10,0,0.000001)
    print("Minimum of g is:",m)

    print("maximum of f is:",maximum(f,-3,3,0.0000001))
    ax = graph(g,-10,0)
    ax.plot(m,g(m),color='red',marker= '*')
    plt.show()