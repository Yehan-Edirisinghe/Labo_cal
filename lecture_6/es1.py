'''Determine the zero of the function g(x) = cos(x) 
    using the bisection method in the interval (0, 4)'''

from math import cos,sqrt
import time

def zero(func, xMin, xMax, prec):
    
    while(sqrt((xMax-xMin)*(xMax-xMin)) > prec):

        avg = (xMax + xMin)/2
        
        if(func(avg)*func(xMin) > 0):
            xMin = avg
        else: 
            xMax = avg
            
    return avg

def rec_zero(func,xMin,xMax,prec):

    # if(func(xMin) == 0): return xMin
    # if(func(xMax) == 0): return xMax
    
    avg = (xMin+xMax)/2

    if(sqrt((xMax-xMin)*(xMax-xMin)) < prec or func(avg) == 0 ): return avg

    if(func(avg)*func(xMin) > 0):
        return rec_zero(func,avg,xMax,prec)
    else:
        return rec_zero(func,xMin,avg,prec)
    


p = .000000000000001

a = time.time()
print(zero(cos,6,0,prec=p))
b = time.time()

c = time.time()
print(rec_zero(cos,6,0,prec=p))
d = time.time()

print("Time for normal method",(b-a))
print("Time for recursive method",(d-c))