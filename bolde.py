import numpy as np
import matplotlib.pyplot as plt

N = 50000

def sturges(sample):

    N = len(sample)
    return int(np.ceil(1+3.322*np.log(N)))

def var(sample):
    s = 0
    m = np.average(sample)
    for i in sample:
        s += (i-m)**2

    return s/(len(sample)-1)

def std(sample):
    return np.sqrt(var(sample))

def skew(sample):

    m = np.average(sample)
    skew = 0
    for i in sample:
        skew += (i - m)**3
    
    return skew/((len(sample)-1)*(std(sample)**3))

def kurt(sample):

    m = np.average(sample)
    skew = 0
    for i in sample:
        skew += (i - m)**4
    
    return skew/((len(sample)-1)*std(sample)**4)

l = []
for i in range(N):

    x,y = np.random.gauss(0,1,2)

    if x > y: l.append(x)
    else : l.append(y)

print('Mean:\t',np.average(l),'\nStand Dev:\t',std(l),'\nSkewness:\t',skew(l),'\nKurtosis:\t',kurt(l))
plt.hist(l,bins=sturges(l))
plt.show()