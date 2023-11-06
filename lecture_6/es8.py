import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

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
    return x**2*y**2

def graph(f,x1,x2,y1,y2):
    
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    x = np.arange(x1,x2,0.05)
    y = np.arange(y1,y2,0.05)
    
    X,Y = np.meshgrid(x,y)
    Z = f(X,Y)
    Z2 = -f(X,Y)

    ax.plot_surface(X,Y,Z)
    # ax.plot_surface(X,Y,Z2)
    
    plt.show()

def min(f,x1,x2,y1,y2,prec = 0.001  ):
    
    r = 4
    
    xm = (x1+x2)/2
    ym = (y1+y2)/2

    while f(xm,ym) - f(xm+r,xm-r) > prec:
    
        p = np.empty((2,4))
        p[0] = (xm-r,xm+r)
        p[1] = (ym-r,ym+r)

        a = f(p[0,0])
        
        for i,j in p:
            if f(p[i,j]) < a:
                a = f(p[i,j])


        xm,ym = a[0],a[1]



    return xm,ym





graph(torus,-6,6,-6,6)

    