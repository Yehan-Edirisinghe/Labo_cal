import random
import matplotlib.pyplot as plt

"Implement a pseudo-random number generator according to a uniform distribution between two arbitrary endpoints."

def plot(y):
    fig,ax = plt.subplots(1,1)
    ax.hist(y,color='salmon',bins=20)
    plt.show()


if __name__ == '__main__':

    N = 100000

    Llimit = 20
    Rlimit = 40


    y=[]

    for i in range(N):
        
        y.append(random.randint(Llimit,Rlimit))

    plot(y)