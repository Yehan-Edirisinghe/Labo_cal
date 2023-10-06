import numpy as np
from exec_time import exec_time
import matplotlib.pyplot as plt

k = 1000000

def init_array(k:int):
    '''returns an ndarray with numbers from 1 to 100'''
    return np.arange(1,k+1,1)

@exec_time
def sum_num(a:np.array):
    '''sums the numbers from one to the index number in the given array'''
    for i in range(1,a.size):
        a[i] = a[i-1]+a[i]
    return a

@exec_time
def sum2(a:np.array):

    return np.cumsum(a)


# print(init_array(k))
sum_num(init_array(k))
sum2(init_array(k))
# print(sum_num(init_array(k)))
# print(sum2(init_array(k)))
