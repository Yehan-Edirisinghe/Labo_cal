import numpy as np

def value_Over_Percentage(l:list, percentage:float):
    '''value below which lies the percentage of the values'''
    
    l.sort()
    lenght = len(l)
    k = int(lenght*percentage)
    return l[k]

def value_Under_Percentage(l, percentage:float):
    '''value under which lies the percentage of the values'''

    l.sort()
    lenght = len(l)
    k = int(lenght*percentage)
    return l[k]

l = list(range(1000))

print(value_Over_Percentage(l,0.25))