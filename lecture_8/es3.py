'''Use the stats class developed during the previous Lectures to compare the standard deviation of 
    the mean calculated for each individual toy with the standard deviation of the sample of means.'''

import stats 
from stats import graph

N = 100
toys = [stats.toy_Gauss.toy(N_max=100) for i in range(N)]

a = graph(toys)
a.show()