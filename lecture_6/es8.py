import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from functions import f,f1
import random as rnd


#sqrt((f(min[0]+r,min[1]+r)-f(min[0],min[1]))**2)

def graph(f,x1,x2,y1,y2):
    
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    x = np.arange(x1,x2,0.05)
    y = np.arange(y1,y2,0.05)
    
    X,Y = np.meshgrid(x,y)
    Z = f(X,Y)

    ax.plot_surface(X,Y,Z)

    return ax

def min(f,x1,x2,y1,y2,prec = 0.001):
    
    
    r = 1/2*sqrt((x2-x1)**2)


    m = ((x1+x2)/2,(y1+y2)/2)
    min = (m[0]+r,m[1]+r)

    while r > prec:

        p = {    (m[0]+r,m[1])
                ,(m[0]-r,m[1])
                ,(m[0],m[1]+r)
                ,(m[0],m[1]-r)
            }
        
        for i in p:

            if f(i[0],i[1]) < f(min[0],min[1]):
                min = i[0],i[1]
        m = min
        r = r/2 + rnd.random()*r

    return min



if __name__ == '__main__':

    center = (0,0)
    r = 5

    x1 = center[0] - r
    x2 = center[0] + r
    y1 = center[1] - r
    y2 = center[1] + r

    func = f

    ax = graph(func,x1,x2,y1,y2)
    m = min(func,x1,x2,y1,y2)

    ax.scatter(m[0],m[1],func(m[0],m[1]), color='red', marker = '*')
    
    # ax.scatter(0,0,func(0,0), color='green', marker = '*')

    plt.show()