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
	
def expo(tau):
	
	return F_inv(random(),tau)


if __name__ == '__main__':
	
	tau = 5
	n = 10000
	fig,ax = plt.subplots(1,1)
	
	x = [expo(tau) for i in range(n)]
	
	ax.hist(x,bins=20)
	plt.show()
