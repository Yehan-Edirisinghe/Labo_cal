import numpy as np

def torus(x,y):
    r = 1
    R = 4
    return -np.sqrt(r**2-(R-np.sqrt((x**2)+(y**2)))**2)

def f(x,y):
    return x*(x-2)*((x**2)-7)

def f1(x,y):
    return -np.power(2.71,-((x+1)**4+y**4))+pow(2.71,-x**2-y**2)

def f2(x,y):
    return .3*np.sin((x+1)*y)-np.power(2.71,-(x**2+y**2))

def f3(x,y):
    return -2.71**(-(x+1)**2-y**2)
