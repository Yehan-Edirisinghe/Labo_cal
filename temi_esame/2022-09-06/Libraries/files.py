import numpy as np


def read_file(path,type = float):

    dati = []
    with open(path, 'r') as file:
        for i in file:
            dati.append(type(i))
    return np.array(dati)

def write_file(path,data):

    with open(path, 'w') as output:
        for i in data:
            output.write(str(i)+'\n')