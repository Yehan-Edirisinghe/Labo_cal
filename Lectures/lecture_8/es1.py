'''Write a program that, given a number N_max, generates N_toys toy experiments, 
    each containing a sample of N_max events following a chosen distribution, and calculates their mean.'''

import numpy as np
import matplotlib.pyplot as plt
from random import random



def gaussian(N_max):

    events = [random() for i in range(N_max)]

    return np.average(events)    

def toyExp(N_max,N_toys):

    toys = [gaussian(N_max) for i in range(N_toys)]

    return toys


if __name__=='__main__':

    N_max = 10000
    N_toys = 1000

    means = toyExp(N_max,N_toys)

    fig,ax = plt.subplots(1,1)
    ax.hist(means)
    plt.show()