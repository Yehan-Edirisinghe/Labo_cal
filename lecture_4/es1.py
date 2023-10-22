
"Write a function that implements the linear congruential generator for pseudo-random numbers, using these parameters:"

M = 2147483647
A = 214013
C = 2531011

def LinearCongGen(x):

    return (A*x + C)%M

class random_generator:
    
    def __init__(self,seed):
        self.seed = seed

    def rand(self):
        return LinearCongGen(self.seed)

if __name__ == '__main__':
    
    for i in range(10):
        print(LinearCongGen(i))