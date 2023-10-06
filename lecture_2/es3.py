import numpy as np

k=100

def even(k):
    '''first k even numbers as ndarray'''
    list = []
    i=2
    while len(list) < k:
        if i%2 == 0:
            list.append(i)
            i+=1
        else:
            i+=1
    return np.array(list)

def odd(k):
    '''first k odd numbers as ndarray'''
    list = []
    i=1
    while len(list) < k:
        if i%2 != 0:
            list.append(i)
            i+=1
        else:
            i+=1
    return np.array(list)

sum = even(k) + odd(k)

# print(even(k))
# print(odd(k))
# print(sum)