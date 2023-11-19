'''Use the stats class developed during the previous Lectures to compare the standard deviation of 
    the mean calculated for each individual toy with the standard deviation of the sample of means.'''

import stats 
from stats import graph
import matplotlib.pyplot as plt

N = 3000
toys = []
toy_stds = []
sample_std = []

for i in range(N):

    toy,stdDev = stats.toy_Gauss.toy(N_max=100)

    toys.append(toy)
    toy_stds.append(stdDev)
    sample_std.append(stats.stdDeviation(toys))


fig,ax = plt.subplots(2,1)

x = range(N)
ax[0].scatter(x,toy_stds)
ax[1].scatter(x,sample_std)

plt.show()