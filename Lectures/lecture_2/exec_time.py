import time

def timer(func):
    '''returns the execution time of argument function'''

    def wrap(*args,**kwargs):
        snap1= time.time()
        result = func(*args,**kwargs)
        snap2= time.time()
        print("Execution time of ",func.__name__," is: ", snap2-snap1)
        return result
    return wrap