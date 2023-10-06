import numpy as np
import random
from exec_time import timer

k = 10000000


def rnd_arr(lenght:int):
    '''generates a np array with random int numbers'''

    arr = []
    for i in range(lenght):
        arr.append(int(random.random()*10))

    return np.array(arr)


@timer
def median(arr):
    arr.sort()
    return arr[int(len(arr)/2)]


def main():
    arr = rnd_arr(k)
    print(median(arr))


main()
