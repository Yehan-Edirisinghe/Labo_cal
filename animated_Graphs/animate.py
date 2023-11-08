import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from math import sqrt,cos

xMax = -1
xMin = 1

def anim(frame):
    return 1

def graph(func):
    
    fig,ax = plt.subplots(1,1)

    an = animation.FuncAnimation(fig,func,fargs =(cos,ax) ,frames=20)
    plt.show()

if __name__=='__main__':

    graph(anim)