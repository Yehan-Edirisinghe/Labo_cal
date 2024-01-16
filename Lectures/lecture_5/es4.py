from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

def file_open(name):
    
    with open(name,'r',) as input:
        list = [float(x.strip('\n')) for x in input]
        return list





if __name__ == '__main__':

    file = 'eventi_unif.txt'
    data = file_open(file)
    
    mean = np.mean(data)

    larger = list(filter(lambda x: x > mean,data))
    smaller = list(filter(lambda x: x < mean,data))

    fig,ax = plt.subplots(1,2)

    ax[0].hist(larger)
    ax[1].hist(smaller)

    print(np.std(data))
    print(np.std(larger))
    print(np.std(smaller))

    plt.show()

    