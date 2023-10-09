import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw

Max_Iterations = 50
width = 500
height = 500

def is_bound(c:complex):

    z = 0+0j
    for i in range(Max_Iterations):
        
        z=z*z + c

        if abs(z) > 2:
            return False
    return True

def manSet(ax):

    x = list(range(width))
    y = list(range(height))

    for i in np.arange(-1,1,2/width):
        for j in np.arange(-1,1,2/height):
            if is_bound(complex(i,j)):
                ax.plot(i,j,marker='.')
                

    

def graph(set):
    fig,ax = plt.subplots(nrows=1,ncols=1)
    for x in range(width):
        for y in range(height):
            if set[x,y] == 1:
                ax.plot(x,y,marker='o')


if __name__ == '__main__':

    fig,ax = plt.subplots(nrows=1,ncols=1)

    manSet(ax)
    plt.show()
    # print(a)
    # graph(a)
    # plt.show()
    # print(np.arange(0,1,.1))