import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from math import sqrt,cos

xMax = -1
xMin = 1

def anim(i,func,ax):

    prec = .001

    while(sqrt((xMax-xMin)*(xMax-xMin)) > prec):

        avg = (xMax + xMin)/2

        ax.clear()
        ax.plot(avg,func(avg))
        
        if(func(avg)*func(xMin) > 0):
            xMin = avg
        else: 
            xMax = avg
    return avg

def graph(func):
    
    fig,ax = plt.subplots(1,1)

    an = animation.FuncAnimation(fig,func,fargs =(cos,ax) ,frames=20)
    plt.show()

if __name__=='__main__':

    graph(anim)