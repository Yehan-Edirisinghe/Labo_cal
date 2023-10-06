import numpy as np

def x_over_25(l):
    '''value below which lies the 25% of the values'''
    l.sort()
    lenght = len(l)
    k = int(lenght*0.25)
    return l[k]

def x_under_25(l):
    '''value under which lies the 25% of the values'''

    l.sort()
    lenght = len(l)
    k = int(lenght*0.75)
    return l[k]


l = list(range(1000))

print(x_under_25(l))