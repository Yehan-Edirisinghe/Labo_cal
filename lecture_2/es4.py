import time
import numpy as np

k=100

a = list(range(k))
b = list(range(k))

def exec_time(func):
    '''this wrapper returns the execution time of argument function'''
    
    def wrap(*args,**kwargs):
        snap1= time.time()
        result = func(*args,**kwargs)
        snap2= time.time()
        print("Execution time of ",func.__name__," is: ", snap2-snap1)
        return result
    return wrap

@exec_time
def compact():
    a1 = np.array(a)
    b1 = np.array(b)
    sum = a1 + b1
    return sum

@exec_time
def noncompact():
    sum = list(range(k))
    for i in range (len (a)):
        sum[i] = a[i] + b[i]
    # print(sum)
    return sum


# print(compact())
# print(noncompact())
