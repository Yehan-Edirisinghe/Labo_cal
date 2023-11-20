import numpy as np
from math import sin,pi
import matplotlib.pyplot as plt
import es5

xmin,xmax,ymax = 0,2*pi,2

def data(N,func):

    areas = []
    errs  = []
    points= []

    for i in [(lambda x: 2**x )(x)for x in range(N)]:

        area,err = (es5.HoM_Area(func,xmin,xmax,ymax,i))

        areas.append(area)
        errs.append(err)
        points.append(i)
    
    return areas,errs,points


if __name__== '__main__':


    N = 15

    fig,ax = plt.subplots(1,3)

    func = lambda x: sin(x)+1

    areas,errs,points = data(N,func)

    x = points


    ax[0].scatter(x,areas)
    ax[0].set_xlabel('N punti')

    ax[1].scatter(x,errs)
    ax[1].set_xlabel('N punti')
    

    ax[2].scatter(x,errs)
    ax[2].set_yscale('log')    
    ax[0].set_xlabel('N punti')


    plt.show()