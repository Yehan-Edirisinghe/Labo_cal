import numpy as np
import matplotlib.pyplot as plt

N = 500000

def sturges(sample):

    N = len(sample)
    return int(np.ceil(1+3.322*np.log(N)))

l = []
for i in range(N):

    x,y = np.random.uniform(0,1,2)

    if x > y: l.append(x)
    else : l.append(y)

plt.hist(l,bins=sturges(l))
plt.show()