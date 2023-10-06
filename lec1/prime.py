import math

def prime(n):
    '''returns list of n primes'''
    primes = [2]
    i=2
    while i <= n:
        for j in primes:
            if i%j ==0:
                i+=1
                break
        primes.append(i)
        i+=1

    return primes

def decomposition(n:int):
    facs = []
    for i in range(2,n):
        if n%i == 0:
            for j in facs:
                if i%j == 0:
                    i+=1
                    break
            facs.append(i)
        i+=1
    return facs

def test(list)->int:
    a=1
    for i in list:
        a*=i
    return a

if __name__ == '__main__':
    # print(prime(100))
    # print(decomposition(24))
    l = decomposition(24)
    print(l)
    print(test(l))