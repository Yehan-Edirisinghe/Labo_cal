import numpy as np
from math import ceil
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from random import random
from scipy.stats import poisson as ps


def F(t,tau):
	return 1-np.exp(-(t/tau))

def F_inv(y,tau):
	return -tau*np.log(1-y)

def exp(tau):
	return F_inv(random(),tau)

def events(tau,tMax):

	if tMax < tau:
		raise Exception("Tempo minore del tempo caratteristico, inserire un tempo valido")
	
	t = 0
	counter = 0
	
	while(t < tMax):
		counter += 1
		t += exp(tau)

	return counter

def poisson(mean,tau=1,N=1000):

	tMax = mean - tau
	return [events(tau,tMax) for i in range(N)]

def variance(list):
	
	sum = 0
	m = np.average(x)

	for i in x:
		sum += (i-m)**2
	
	return sum/len(x)

def skewness(list):
	return 1/np.sqrt(np.average(list))

def kurtosis(list):
	return 1/np.average(list)

def update(val):

	N = int(NSlider.val)
	mean = MSlider.val
	x = poisson(mean=mean,N=N)
	ax.clear()
	ax.legend([1],["Kurtosis: {kurtosis(x)}"])
	ax.hist(x, bins= sturges(x),label= f'Kurtosis = {kurtosis(x)}\nskewness = {skewness(x)}')
	ax.legend()

def sturges(sample):
    '''returns the surges function applied to the sample length'''

    N = len(sample)
    return ceil(1+3.322*np.log(N))

if __name__ == '__main__':
	
	
	fig,ax = plt.subplots(1,1)
	plt.subplots_adjust(bottom=0.35)

	meanax = plt.axes([0.15, 0.2, 0.7, 0.03])
	Nax = plt.axes([0.15, 0.25, 0.7, 0.03])
	tax = plt.axes([0.15, 0.15, 0.7, 0.03])
	
	
	# print("Average\t",np.average(x))
	# print("Skewness\t",skewness(x))
	# print("Kurtosis\t",kurtosis(x))
	
	MSlider = Slider(meanax,"Mean",2,100,30)
	NSlider = Slider(Nax,"N",100.0,2000.0,300)
	TSlider = Slider(tax,"Tau",1,200.0,1)
	
	NSlider.on_changed(update)
	MSlider.on_changed(update)
	TSlider.on_changed(update)


	x = poisson(MSlider.val,TSlider.val,NSlider.val)
	ax.hist(x,bins=int(len(x)/20), label= f'Kurtosis = {kurtosis(x)}\nskewness = {skewness(x)}')
	ax.legend()
	plt.show()