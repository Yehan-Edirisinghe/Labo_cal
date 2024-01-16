from es1 import rec_zero
from es4 import minimum,maximum
import matplotlib.pyplot as plt
import numpy as np
from math import cos

def func(x):
    return cos(x)

def graph(func,range):

    fig,ax = plt.subplots(1,1)

    x = np.linspace(range[0],range[1],200)
    y = [func(i) for i in x]
    
    ax.plot(x,y)
    a = minimum(func,range[0],range[1],0.0001)
    b = maximum(func,range[0],range[1],0.0001)
    c = rec_zero(func,range[0],range[1],0.0001)

    ax.plot(a,func(a),color='red',marker='*')
    ax.plot(b,func(b),color='red',marker='*')
    ax.plot(c,func(c),color='red',marker='*')

    plt.show()

if __name__ == '__main__':

    graph(func,(-4,4))