import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw

Max_Iterations = 60
width = 100
height = 100

def is_bound(c:complex):

    z = 0j
    for i in range(Max_Iterations):
        z=z*z + c
        if abs(z) > 2:
            return False
    return True

def manSet():
    a = np.zeros((width,height))
    i=0
    while i < width:
        j=0
        while j<height:

            if is_bound(complex(i,j)) == True:
                a[i,j] = 1
                j+=1
                
            else:
                a[i,j] = 0
                j+=1
        i+=1

    return a

def graph(set):
    fig,ax = plt.subplots(nrows=1,ncols=1)
    for x in range(width):
        for y in range(height):
            if set[x,y] == 1:
                ax.plot(x,y,marker='o')


if __name__ == '__main__':

    a=manSet()
    print(a)
    # graph(a)
    # plt.show()