import numpy as np
import matplotlib.pyplot as plt
N = 100

def is_bound(c:complex):
    z = 0j
    for i in range(N):
        z=z*z + c
    if abs(z) > 2:
        return False
    else:
        return True

def Manset(N):
    a = np.array((N,N))
    i=0
    while i < N:
        j=0
        while j<N:
            if is_bound(complex(i,j)):
                a[i,j] = 1
            else:
                a[i,j] = 0

    return a



if __name__ == '__main__':

    print(Manset(100))

