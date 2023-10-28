from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from math import ceil

def file_open(name):
    
    with open(name,'r',) as input:
        list = [float(x.strip('\n')) for x in input]
        return list


def sturges(sample):
    '''returns the surges function applied to the sample length'''

    N = len(sample)
    return ceil(1+3.322*np.log(N))


if __name__ == '__main__':

    file = 'eventi_gauss.txt'
    data = file_open(file)
    
    squared = list(map(lambda x: x**2,data))
    cubed = list(map(lambda x: x**3,data))

    fig,ax = plt.subplots(1,3)

    ax[0].hist(data, bins=sturges(data))
    ax[1].hist(squared, color = 'red',bins=sturges(squared),label='squared')
    ax[2].hist(cubed, color = 'green',bins=sturges(cubed),label='cubed')
    
    ax[1].legend()
    ax[2].legend()

    plt.show()