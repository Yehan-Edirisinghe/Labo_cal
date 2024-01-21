import numpy as np

def max_sez_aurea(func,xmin,xmax,*args,prec=.0001,min=False,**kwargs):
    '''f = f(x,*args)\n
    for minimum put min=True'''

    r = (-1+np.sqrt(5))/2  #golden ratio

    while abs(xmax-xmin) > prec:

        a = xmin +     r* abs(xmax-xmin)
        b = xmin + (1-r)* abs(xmax-xmin)
        
        if min==False:
            if func(b,*args,**kwargs) < func(a,*args,**kwargs):
                xmin = b
            else: 
                xmax = a
        else:
            if func(b,*args,**kwargs) > func(a,*args,**kwargs):
                xmin = b
            else: 
                xmax = a

    return xmin,func(xmin,*args,**kwargs)

def Hit_or_miss(f,xmin,xmax,ymax,N, *args,**kwargs) -> tuple:
    '''returns integral value and error\n
    f = f(x,*args)'''

    counter = 0
    for i in range(N):
        x = np.random.uniform(xmin,xmax)
        y = np.random.uniform(0,ymax)
        if y < f(x,*args,**kwargs):
            counter += 1
    
    p = counter/N
    A = (xmax-xmin)*ymax
    var = A**2*p*(1-p)/N

    return A*p, np.sqrt(var)

def Montecarlo(f,xmin,xmax,N,*args,**kwargs) -> tuple:
    '''returns integral value and error\n
    f = f(x,*args)'''

    g = [f(np.random.uniform(xmin,xmax), *args,**kwargs) for i in range(N)]

    integ = (xmax-xmin)*np.mean(g)
    sigma = (xmax-xmin)*np.sqrt(np.var(g)/N)

    return integ,sigma

def rand_TAC(xmin,xmax,ymax,*args,**kwargs):
    '''returns r.v. ~ f(x,args)'''
    x = np.random.uniform(xmin,xmax)
    y = np.random.uniform(0,ymax)
    if f(x,*args,**kwargs) < y:
        return rand_TAC(xmin,xmax,ymax,*args,**kwargs)
    return x

if __name__ == '__main__':

    ###EXAMPLE###

    import matplotlib.pyplot as plt

    def f(x,a,b):
        return np.sin(a*x)+b
    

    x = np.linspace(0,2*np.pi)
    plt.plot(x,f(x,1,0))
    
    xmax,ymax = max_sez_aurea(f,0,np.pi,min=False,a=1,b=0)
    xmin,ymin = max_sez_aurea(f,np.pi,2*np.pi,1,0,min=True)

    plt.scatter(xmax,ymax, c='r')
    plt.scatter(xmin,ymin, c='g')

    print("Integral HoM:",          Hit_or_miss(f,0,np.pi,1,1000,1,0))
    print("Integral Montecarlo:",   Montecarlo(f,0,np.pi,1000,1,0))

    plt.show()