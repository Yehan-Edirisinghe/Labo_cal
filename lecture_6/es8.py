import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def f(x,y):
    return -np.sqrt(1-(x**2)-(y**2))

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


def graph(f,x1,x2,y1,y2):
    
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    x = np.arange(x1,x2,0.005)
    y = np.arange(y1,y2,0.005)
    
    X,Y = np.meshgrid(x,y)
    Z = f(X,Y)

    ax.plot_surface(X,Y,Z)
    # ax.plot_surface(X,Y,Z2)

    return ax

def min(f,x1,x2,y1,y2,prec = 0.001):
    
    r = 1/5
    r = r*sqrt((x2-x1)**2)


    m = ((x1+x2)/2,(y1+y2)/2)
    min = (m[0]+r,m[1]+r)

    while sqrt((f(m[0],m[1])-f(min[0],min[1]))**2) > prec:

        p = {    (m[0]+r,m[1])
                ,(m[0]-r,m[1])
                ,(m[0],m[1]+r)
                ,(m[0],m[1]-r)
            }
        
        for i in p:

            if f(i[0],i[1]) < f(min[0],min[1]):
                min = i[0],i[1]
        m = min

    return min

    #calcolo distanza tra punto minimo e punto medio
    #se sotto precisione ho trovato il valore
    #altrimenti reitero togliendo un intervallo


if __name__ == '__main__':
    k = 1
    ax = graph(f,-k,k,-k,k)
    m = min(f,-k,k,-k,k)

    ax.scatter(m[0],m[1],f(m[0],m[1]), color='red', marker = '*')
    # ax.scatter(0,0,f(0,0), color='green', marker = '*')

    plt.show()