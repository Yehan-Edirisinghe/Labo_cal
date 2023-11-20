'''Use the stats class developed during the previous Lectures to compare the standard deviation of 
    the mean calculated for each individual toy with the standard deviation of the sample of means.'''

'''Use two scatter plots to compare the evolution of the standard deviation of the mean calculated for each individual toy 
    with the standard deviation of the sample of means as the number of events generated in a single toy experiment varies.'''

import stats 
from stats import graph
import matplotlib.pyplot as plt

N = 1000
toys = []       #medie di ogni toy experiment
toy_stds = []   #deviazioni standard dei toy exp
sample_std = [] #deviazione standard delle medie

for i in range(N):

    toy,stdDev = stats.toy_Gauss.toy(N=1000)

    toys.append(toy)
    toy_stds.append(stdDev)
    sample_std.append(stats.stdDeviation(toys))


fig,ax = plt.subplots(2,1)

x = range(N)
ax[0].scatter(x,toy_stds)
ax[1].scatter(x,sample_std)

plt.show()