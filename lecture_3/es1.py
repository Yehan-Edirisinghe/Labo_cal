import matplotlib.pyplot as plt
import numpy as np
import sys



def file():
    '''opens the input file and outputs a list with the values as float'''
    sample = []
    with open(sys.argv[1],'r') as input_file:
        for i in input_file:
            sample.append(i)
    return sample

def positive(sample):
    '''prints the first 10 positive elements'''

    pos = []
    for i in sample:
        if i>=0:
            pos.append(i)
    for j in range(10):
        print(pos[j])

def count(sample):
    '''returns the number of elements in the file'''
    return len(sample)

def hist_N(sample,N:int):
    tmp = []
    for i in range(len(sample)):
        if i<= N:
            tmp.append(i)
    fig,ax = plt.subplots(nrows=1,ncols=1)
    ax.hist(sample,color='orange')
    plt.show()

def hist(sample):
    fix,ax = plt.subplots(nrows= 1, ncols=1)
    ax.hist(sample,color = 'orange')
    plt.show()



if __name__ == '__main__':
    samples = file()
    # positive(samples)
    print(count(samples))
    # hist_N(samples,1)