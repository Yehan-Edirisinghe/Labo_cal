import exponential as exponential
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button
import numpy as np



def events(tau,tMax):
	t = 0
	counter = 0
	while(t < tMax):
		counter += 1
		t += exponential.exp(tau)
	return counter

def distr(N,tau,tMax):
	return [events(tau,tMax) for i in range(N)]

def mean(x):
	return np.sum(x)/len(x)

def variance(x):
	sum = 0
	m = mean(x)
	for i in range(len(x)):
		sum += (x-m)**2
	return sum/len(x)

if __name__ == '__main__':
	
	tau = .3
	tMax = 60
	N = 1000

	counts = distr(N,tau,tMax)

	print(np.sqrt(mean(counts)))

	fig,ax = plt.subplots(1,1)
	ax.hist(counts,bins=int(len(counts)/50))
	plt.show()