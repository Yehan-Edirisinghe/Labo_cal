import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,pi,cos,sin
import functions as f
import random as rnd

def graph(f,x1,x2,y1,y2):

    '''plots the graph of a given function'''
    #boundaries must be increasing in size

    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    x = np.arange(x1,x2,0.05)
    y = np.arange(y1,y2,0.05)
    
    X,Y = np.meshgrid(x,y)
    Z = f(X,Y)

    ax.plot_surface(X,Y,Z, alpha=.2)

    return ax

def points(m,k,r):

    p = []

    for i in range(k):

        p.append((m[0]+r*cos((2*pi*i)/k),m[1]+r*sin((2*pi*i)/k)))
    
    return p

def min(f,x1,x2,y1,y2,prec = 0.001):
    
    buffer = []

    r = .5*abs(x2-x1)


    m = ((x1+x2)/2,(y1+y2)/2)
    min = (m[0]+r,m[1]+r)

    while r > prec:


        p = points(m,10,r)
                
        for i in p:

            #il valore deve restare nell'intervallo del dominio e deve essere più piccolo
            if f(i[0],i[1]) < f(min[0],min[1]) and i[0]<x2 and i[0]>x1 and i[1]<y2 and i[1]>y1:
                min = i
        
        buffer.append(min)
        
        m = min
        r *= (0.35+rnd.random())

    return min,buffer


if __name__ == '__main__':

    center = (0,0)
    r = 4

    x1 = center[0] - r
    x2 = center[0] + r
    y1 = center[1] - r
    y2 = center[1] + r

    func = f.f2

    ax = graph(func,x1,x2,y1,y2)

    
    m,buffer = min(func,x1,x2,y1,y2)


    ax.scatter(m[0],m[1],func(m[0],m[1]), color='red', marker = '*')
    
    for i in buffer:
        ax.scatter(i[0],i[1],func(i[0],i[1]),color='green',marker='*')

    plt.show()