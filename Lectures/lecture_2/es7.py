import numpy as np
import math

l = [1,2,3,4,5,4,3,2,3,2,5,6,4,2,3]

def mean(a):
        return sum(a)/len(a)

def variance(l):
        m = mean(l)
        sum = 0
        for i in range(len(l)):
                sum += (l[i]-m)*(l[i]-m)

        return (sum)/len(l)

def std_dev(l):
        return math.sqrt(variance(l))


print(np.var(l))
print(variance(l))
print(std_dev(l))
