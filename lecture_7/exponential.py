import numpy as np
from math import log
import matplotlib.pyplot as plt
from random import random

def f(t,tau):
	return np.exp(-t/tau)/tau

def F(t,tau):
	return 1-np.exp(-(t/tau))

def F_inv(y,tau):
	return -tau*np.log(1-y)

def exp(tau):
	return F_inv(random(),tau)





if __name__ == '__main__':
	
	tau = 10
	n = 10000
	fig,ax = plt.subplots(1,1)
	
	x = [exp(tau) for i in range(n)]
	
	ax.hist(x,bins=int(len(x)/50))
	plt.show()