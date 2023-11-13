import es1
import matplotlib.pyplot as plt

def events(tau,tMax):
	t = 0
	counter = 0
	while(t < tMax):
		counter += 1
		t += es1.expo(tau)
	return counter

def distr(N,tau,tMax):
	
	return [events(tau,tMax) for i in range(N)]

	
		

if __name__ == '__main__':
	
	tau = 5
	tMax = 100
	N = 500000
	
	
	list = distr(N,tau,tMax)
			
	
	fig,ax = plt.subplots(1,1)
	ax.hist(list,bins=20)
	plt.show()
