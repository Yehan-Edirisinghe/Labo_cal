import numpy as np
from math import sin

def fun_1(x, y):
    return x**2 / np.sqrt(x**2 + y**2)

def fun_2(x, y):
    return x / np.sqrt(x**2 + y**2)

def fun_3(x, y):
    return x**2 * y / (x**4 + y**2)

def fun_4(x, y):
    return x * y / (x**2 + y**2)

def torus(x,y):
    r = 1
    R = 4
    return np.sqrt(r**2-(R-np.sqrt((x**2)+(y**2)))**2)

def f(x,y):
    return np.sin(x+y)*pow(2.71,-x**2)

def f1(x,y):
    return -pow(2.71,-((x)**4+y**4))+pow(2.71,-x**2-y**2)