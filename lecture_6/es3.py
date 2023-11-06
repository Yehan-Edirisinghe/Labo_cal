'''Implement a function that calculates the factorial of a number 
    using a recursive function.'''

def factorial(x):
    if(x == 0):
        return 1
    if(x == 1): 
        return x
    return x*factorial(x-1)

print(factorial(0))
