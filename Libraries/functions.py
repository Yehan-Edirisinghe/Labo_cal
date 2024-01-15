import numpy as np

def max_sez_aurea(func,xmin,xmax,*args,prec=.0001):
    '''func of type f(x,args)'''
    r = (-1+np.sqrt(5))/2  #golden ratio

    while abs(xmax-xmin) > prec:

        a = xmin +     r* abs(xmax-xmin)
        b = xmin + (1-r)* abs(xmax-xmin)
        
        if func(b,*args) < func(a,*args):
            xmin = b
        else: 
            xmax = a

    return xmin,func(xmin,*args)


if __name__ == '__main__':

    def f(x,a,b):
        return np.sin(a*x)+b

    x,y = max_sez_aurea(f,0,np.pi, np.pi,0)
    print(x,y)