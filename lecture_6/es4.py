from math import sqrt

'''Determine the minimum of the function g(x) = x2 + 7.3x + 4 
    using the golden ratio search method in the interval (-10, 10).'''

r = (-1+sqrt(5))/2

def f(x):

    return -((x-1)**2)

def g(x):
    return x**2 + (7.3*x) +4

def minimum(func,xmin,xmax,precision):
    
    if(sqrt((xmax-xmin)**2) < precision):
        return xmin
    
    x2 = xmin +     r*(xmax-xmin)
    x3 = xmin + (1-r)*(xmax-xmin)
    
    if(func(x3) > func(x2)):
        return minimum(func,x3,xmax,precision)
    else:
        return minimum(func,xmin,x2,precision)

def maximum(func,xmin,xmax,precision):
    
    d = sqrt((xmax-xmin)**2)

    if(d < precision):
        return xmin
    
    x2 = xmin +     r* d
    x3 = xmin + (1-r)* d
    
    if(func(x3) < func(x2)):
        return maximum(func,x3,xmax,precision)
    else:
        return maximum(func,xmin,x2,precision)



if __name__ == '__main__':

    print("Minimum of g is:",minimum(g,-10,0,0.000001))

    print("maximum of f is:",maximum(f,-3,3,0.0000001))