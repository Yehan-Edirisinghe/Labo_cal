import numpy as np
import files as f

def linear(x,y):

    A,B = 0,0
    N = len(x)

    xi = np.sum(x)
    xi2 = np.sum(x**2)
    yi = np.sum(y)
    xyi = np.sum(x*y)

    A = (yi*xi2-xi*xyi)/(N*xi2-xi**2)

    B = (N*xyi-xi*yi)/(N*xi2-xi**2)


    return A,B

if __name__ == '__main__':

    x = np.linspace(0,3,100)
    
    y = 0.3*x+1

    A,B = linear(x,y)

    print(A,B)