import sys
sys.path.insert(1,'/home/unicorn/Documents/Labo_cal')
from Libraries.interpolazione import linear
import numpy as np
import matplotlib.pyplot as plt
import es5


def data(func,xmin,xmax,ymax,N):

    areas   = []
    errs    = []
    points  = []

    for i in [(lambda x: 2**x )(x) for x in range(N)]:
    # for i in range(1,N):


        area,err = (es5.HoM_Area(func,xmin,xmax,ymax,i))

        areas.append(area)
        errs.append(err)
        points.append(i)
    
    return areas,errs,points


if __name__== '__main__':


    N = 12
    xmin,xmax,ymax = 0, 2*np.pi, 2

    fig,ax = plt.subplots(1,3)

    func = lambda x: np.sin(x)+1

    areas,errs,x = data(func,xmin,xmax,ymax,N)

    A,B = linear(x,np.log(errs))

    # f = file('sample.txt').write(areas)

    ax[0].scatter(x,areas)
    ax[0].set_title('Areas')
    ax[0].set_xlabel('N punti')
    ax[0].set_ylabel('Area')

    ax[1].scatter(x,errs)
    ax[1].set_title('Errors')
    ax[1].set_xlabel('N punti')
    ax[1].set_ylabel('errore')

    ax[2].scatter(x,np.log(errs))
    ax[2].set_title('Log Err')
    ax[2].set_xlabel('N punti')
    ax[2].set_ylabel('errore')

    ax[2].plot()
    # ax[2].set_xscale('log')    

    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()

    plt.show()