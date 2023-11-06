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

    x = np.arange(x1,x2,0.005)
    y = np.arange(y1,y2,0.005)
    
    X,Y = np.meshgrid(x,y)
    Z = f(X,Y)
    Z2 = -f(X,Y)

    ax.plot_surface(X,Y,Z)
    # ax.plot_surface(X,Y,Z2)

    return ax

def min(f,x1,x2,y1,y2,m=None,prec = 0.001):
    
    r = (sqrt(5)-1)/2
    r = r*(x2-x1)

    if m == None:
        m = ((x1+x2)/2,(y1+y2)/2)
    
    p1 = (m[0]+r,m[1])
    p2 = (m[0]-r,m[1])
    p3 = (m[0],m[1]+r)
    p4 = (m[0],m[1]-r)

    p = {p1,p2,p3,p4}
    min = (p1[0],p1[1])

    if sqrt(f(m[0],m[1])-f(min[0],min[1]))**2 < prec:
        return m[0],m[1]
    
    
    for i in p:

        if f(i[0],i[1]) < f(min[0],min[1]):
            min = i[0],i[1]
    a = 1
    b = 1
    c = 1
    d = 1

    return min(f,a,b,c,m=(2,3))

    #calcolo distanza tra punto minimo e punto medio
    #se sotto precisione ho trovato il valore
    #altrimenti reitero togliendo un intervallo


if __name__ == '__main__':

    ax = graph(fun_1,-6,6,-6,6)
    print(min(fun_1,-6,6,-6,6))
    plt.show()