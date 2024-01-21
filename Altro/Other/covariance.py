import numpy as np

def f_no_Corr(N):

    x = np.random.uniform(0,np.pi,N)
    # y = np.random.uniform(0,1,N)
    y = np.random.normal(0,1,size=N)

    # y = np.array([np.sin(i*(5+np.random.uniform(0,.25))) for i in x])

    return x,y

def f_yes_Corr(N):

    x = np.random.normal(0,1,size=N)
    # y = x*np.random.random(N)
    y = np.array([(i*(5+np.random.uniform(0,.35))) for i in x])

    return x,y

def cov(x,y):
    '''returns covariance of x,y'''

    sum = 0
    m = np.average(x)
    n = np.average(y)

    for i in range(len(x)):
        
        sum += (x[i]-m)*(y[i]-n)

    return sum/len(x)

def covMatrix(x,y):
    '''returns covariance matrix \n\n
    x and y are ndarrays'''

    mat = np.empty((2,2))

    mat[0,0] = cov(x,x)
    mat[0,1] = cov(x,y)
    mat[1,0] = cov(y,x)
    mat[1,1] = cov(y,y)

    r = mat[1,0]*mat[0,1]/(mat[0,0]*mat[1,1])

    return mat,r**2

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    
    fig,ax = plt.subplots(1,2)

    x1,y1 = f_no_Corr(2000)
    x2,y2 = f_yes_Corr(2000)

    a,r = covMatrix(x1,y1)
    b,r2 = covMatrix(x2,y2)

    ax[0].scatter(x1,y1)
    ax[0].set_xlabel(r)

    ax[1].scatter(x2,y2)
    ax[1].set_xlabel(r2)

    plt.show()