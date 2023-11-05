'''Determine the minimum of the function g(x) = x2 + 7.3x + 4 
    using the golden ratio search method in the interval (-10, 10).'''

#   x_zero = -3.65

from math import sqrt

def g(x):
    return x*x + 7.3*x +4

def minimum(func,xmin,xmax,precision):

    r = (-1+sqrt(5))
    
    if(sqrt((xmax-xmin)*(xmax-xmin)) < precision):
        return xmin
    
    x2 = xmin +     r*(xmax-xmin)
    x3 = xmin + (1-r)*(xmax-xmin)
    
    if(func(x3) < func(x2)):
        return minimum(func,xmin,x3,precision)
    else:
        return minimum(func,x2,xmax,precision)
    

print(minimum(g,-10,10,0.01))