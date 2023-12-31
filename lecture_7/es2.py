import poisson
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button
import numpy as np

def events(tau,tMax):

	if tMax < tau:
		raise Exception("Tempo minore del tempo caratteristico, inserire un tempo valido")
	
	t = 0
	counter = 0
	
	while(t < tMax):
		counter += 1
		t += poisson.exp(tau)

	return counter

def distr(N,tau,tMax):
	return [events(tau,tMax) for i in range(N)]

def mean(x):
	return np.average(x)

def variance(x):

	sum = 0
	m = np.average(x)

	for i in x:
		sum += (i-m)**2
	
	return sum/len(x)

def sigma(x):
	return np.sqrt(variance(x))


if __name__ == '__main__':
	
	tau = 1
	tMax = 50
	N = 10000

	counts = distr(N,tau,tMax)

	print(mean(counts))
	print(variance(counts))

	fig,ax = plt.subplots(1,1)
	ax.hist(counts,bins=int(len(counts)/100))
	plt.show()