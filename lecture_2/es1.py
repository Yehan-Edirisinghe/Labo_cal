import numpy as np

def first():
    list = [3,4,5]
    arr = np.array(list)
    print(arr)

def second():
    arr = np.zeros(3)
    print(arr)

def third():
    var1 = 2
    var2 = 4
    var3 = True
    arr = np.arange(var1,var2,1)
    print(arr)

first()
second()
third()
