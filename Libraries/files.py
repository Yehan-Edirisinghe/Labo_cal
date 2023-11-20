import numpy as np


class file:

    def __init__(self,path,npArray=True):
        
        self.path = path
        
        try:
            self.sample = self.get(npArray)
        except IOError:
            pass

    def get(self,npArray = True):

        
        if npArray == True:

            with open(self.path, 'r') as file:
                sample_np = np.array([float(x) for x in file.readlines()])

            return sample_np

        else:

            with open(self.path, 'r') as file:

                sample_list = [float(x) for x in file.readlines()]
        
            return sample_list
        
    def write(self, sample):

        with open(self.path, 'w') as file:
            
            for i in sample:

                file.write(str(i)+'\n')




if __name__ == '__main__':

    path = '/home/peppo/Documents/Labo_cal/eventi_gauss.txt'

    f = file(path)
    array = f.sample
    
    g = file('test.txt')
    g.write(array)

    print(array)