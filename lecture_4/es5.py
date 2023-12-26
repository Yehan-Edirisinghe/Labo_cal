'''Implement a pseudo-random number generator that uses the try-and-catch method
     to generate pseudo-random numbers according to an arbitrary probability distribution'''

import random
import matplotlib.pyplot as plt
from scipy.stats import norm


def rand(xMin, xMax) :
    
    return xMin + random.random() * (xMax - xMin)

def rand_TAC(f, xMin, xMax, yMax) :
    
    x,y = rand(xMin, xMax) , rand(0, yMax)
    

    while (y > f(x)) :
        x = rand(xMin, xMax)
        y = rand(0, yMax)
    return x


if __name__ == '__main__':

    x =[]

    N=1000
    
    for i in range(N):
        
        x.append(rand_TAC(norm.pdf,-10,10,2))
    
    fig,ax = plt.subplots(1,1)
    ax.hist(x,bins=20)
    plt.show()

