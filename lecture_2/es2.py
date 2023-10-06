import numpy as np
from exec_time import timer
import matplotlib.pyplot as plt

k = 1000000

def init_array(k:int):
    '''returns a numpy array with numbers from 1 to 100'''
    return np.arange(1,k+1,1)

@timer
def sum_num(a:np.array):
    '''sums the numbers from one to the index number in the given array'''
    for i in range(1,a.size):
        a[i] = a[i-1]+a[i]
    return a

@timer
def sum2(a:np.array):
    '''sums the numbers from one to the index number in the given array'''
    return np.cumsum(a)


sum_num(init_array(k))
sum2(init_array(k))

# print(sum_num(init_array(k)))
# print(sum2(init_array(k)))