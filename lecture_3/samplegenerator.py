import numpy as np
from numpy import pi
import random
import math

k = 10000
sample = []

for i in range(k):
    sample.append(pi + random.random())
print(sample)


with open('sample.txt', 'w') as output:
    for i in sample:
        output.write(str(i) + '\n')
        