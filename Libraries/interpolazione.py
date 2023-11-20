import numpy as np


def linear(x,y):

    A,B = 0,0
    N = len(x)

    xi = np.sum(x)
    
    xi2 = np.sum([i**2 for i in x])
    yi = np.sum(y)
    xy = x*y
    xyi = np.sum(xy)

    A = (yi*xi2-xi*xyi)/(N*xi2-xi**2)

    B = (N*xyi-xi*yi)/(N*xi2-xi**2)


    return A,B

if __name__ == '__main__':

    x = np.linspace(0,5,100)

    y = 0.3*x+1

    A,B = linear(x,y)

    print(A,B)