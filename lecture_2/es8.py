import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

fig,ax = plt.subplots(nrows= 1, ncols= 1)

def sin_cos():
    # plots sin(x) and cos(x)
    x = np.linspace(0,2*pi,10000)       #creates the x axis values
    sin = np.sin(x)                     #creates the y axis values
    cos = np.cos(x)
    ax.plot(x,sin, label='Sin(x)')
    ax.plot(x,cos, label='Cos(x)')
    ax.set_title('Comparison sin and cos')
    ax.set_xlabel('x',loc='right')
    ax.set_ylabel('y',loc='top')
    ax.legend()
    plt.xticks([pi/2,pi,3/2*pi,2*pi])   #changes the x axis scale
    

def A_B_term(A=0,B=0):
    '''plots sin(x) and sin(x-A)+B'''

    x = np.linspace(0,2*pi,10000)
    sin1 = np.sin(x-A)+B
    sin = np.sin(x)
    ax.plot(x,sin, label='Sin(x)')
    ax.plot(x,sin1, label='Sin(x-A)+B')    
    ax.set_title('Comparison sin and cos')
    ax.set_xlabel('x',loc='right')
    ax.set_ylabel('y',loc='top')
    ax.legend()
    plt.xticks([pi/2,pi,3/2*pi,2*pi])

def C_D_term(C=1,D=1):
    '''plots cos(x) and Dcos(Cx)'''

    x = np.linspace(0,2*pi,10000)
    cos1 = D*np.cos(C*x)
    cos = np.cos(x)
    ax.plot(x,cos, label='Sin(x)')
    ax.plot(x,cos1, label='D Sin(Cx)')    
    ax.set_title('Comparison sin and cos')
    ax.set_xlabel('x',loc='right')
    ax.set_ylabel('y',loc='top')
    ax.legend()
    plt.xticks([pi/2,pi,3/2*pi,2*pi])


# sin_cos()
# A_B_term(pi,3)
C_D_term(1,2)

plt.show()