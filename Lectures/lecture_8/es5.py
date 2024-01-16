'''Implement the hit-or-miss integration method with the example function f(x) = sin(x)'''

import numpy as np
from math import sin,pi


def hit_or_miss(func,point:tuple):

    if point[1] <= func(point[0]):
        return True
    else: 
        return False


def HoM_Area(func,xmin,xMax,yMax,N):

    counter = 0
    for i in range(N):

        x = np.random.uniform(xmin,xMax)
        y = np.random.uniform(0,yMax)

        if hit_or_miss(func,(x,y)):
            
            counter += 1
        
    p = counter/N
    A = abs(xmin-xMax)*yMax

    err = np.sqrt((A**2*p*(1-p))/N)

    return p*A,err


if __name__=='__main__':

    N = 10000
    
    func = lambda x: sin(x)+1

    I = HoM_Area(func,0,pi,2,N)

    print(I)