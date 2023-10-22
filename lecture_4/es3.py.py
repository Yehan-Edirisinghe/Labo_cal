import random


"Show that initializing the seed of a pseudo-random integer generator is equivalent to looking into a sequence of pseudo-random numbers at any point."

def rand(seed):

    list = []
    print(f"Starting at seed: {seed}")
    
    for i in range(4):
        random.seed(seed+i)
        list.append(random.random())

    return list



if __name__ == '__main__':
    seed = 1

    print(rand(seed),"\n")
    print(rand(seed+1),"\n")
    print(rand(seed+2),"\n")
    print(rand(seed+3),"\n")