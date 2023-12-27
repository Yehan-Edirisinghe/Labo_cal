import numpy as np
import matplotlib.pyplot as plt


def rand_exp(to):

    return -to*np.log(1-np.random.uniform())

def exp_pdf(to,N):

    d = np.zeros(N)
    for i in range(N):
        d[i] = rand_exp(to)
    
    return d,np.average(d)

def estimator_bias(N,n=100):

    means = np.zeros(N)

    for i in range(N):
        
        means[i] = exp_pdf(5,n)[1]
    
    est_mean = np.average(means)
    est_std = np.std(means)

    print(f"Mean of the means:\t{est_mean}")
    print(f"Std of the means:\t{est_std}")

    plt.hist(means)
    plt.show()

    return est_mean,est_std

estimator_bias(1000)