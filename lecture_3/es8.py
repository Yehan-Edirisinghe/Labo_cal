import es
import numpy as np
import matplotlib.pyplot as plt



def exponential():
    x = np.arange(-3,3,.5)
    y = np.exp(x)
    return x,y


if __name__ == '__main__':
    
    x,y = exponential()
    fig,ax1 = plt.subplots(nrows=1,ncols=2)
    ax1[0].plot(x,y)
    es.cumulativeDF(y,es.mean(y),es.stdDeviation(y),ax=ax1[1])
    plt.show()