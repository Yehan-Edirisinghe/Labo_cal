import numpy as np
import matplotlib.pyplot as plt
import es5
import Libraries.files as files

xmin,xmax,ymax = 0,2*np.pi,2

def data(N,func):

    areas   = []
    errs    = []
    points  = []

    # range = [(lambda x: 2**x )(x)for x in range(N)]

    for i in range(1,N,10):


        area,err = (es5.HoM_Area(func,xmin,xmax,ymax,i))

        areas.append(area)
        errs.append(err)
        points.append(i)
    
    return areas,errs,points


if __name__== '__main__':


    N = 1200

    fig,ax = plt.subplots(1,3)

    func = lambda x: np.cos(x)+1

    areas,errs,x = data(N,func)

    f = files('sample.txt').write(areas)

    ax[0].scatter(x,areas)
    ax[0].set_title('Areas')
    ax[0].set_xlabel('N punti')
    ax[0].set_ylabel('Area')

    ax[1].scatter(x,errs)
    ax[1].set_title('Errors')
    ax[1].set_xlabel('N punti')
    ax[1].set_ylabel('errore')

    ax[2].scatter(x,errs)
    ax[2].set_title('Log Err')
    ax[2].set_xlabel('N punti')
    ax[2].set_ylabel('errore')

    ax[2].set_xscale('log')    

    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.show()