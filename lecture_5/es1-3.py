from sys import exit
import numpy as np
from math import gcd


class Fraction:
    
    def __init__(self,num,den):
        
        
        if den == 0:
            print("Can't have 0 as denominator")
            exit()
        com_Div = gcd(num,den)
        self.num = num // com_Div
        self.den = den // com_Div

    def __add__(self,fraction):

        n = self.num * fraction.den + fraction.num * self.den
        d = self.den * fraction.den
        
        return Fraction(n,d)
    
    def __sub__(self,fraction):

        n = self.num * fraction.den - fraction.num * self.den
        d = self.den * fraction.den
        
        return Fraction(n,d)

    def __mul__(self,f):

        n = self.num * f.num
        d = self.den * f.den
        return Fraction(n,d)

    def __truediv__(self,f):

        n = self.num * f.den
        d = self.den * f.num
        return Fraction(n,d)
    
    def print(self):        
        return self.num/self.den
    
def Test():

    first = Fraction(2,5)
    second = Fraction(1,2)

    print(f"Prima frazione:  {first.print()}")
    print(f"Seconda frazione:  {second.print()}\n")

    somma   = first+second
    sott    = first-second
    prod    = first+second
    div     = first/second

    print(f"Somma:\t\t{somma.num}\t\t{somma.den}")
    print(f"Sottrazione:\t\t{sott.num}\t\t{sott.den}")
    print(f"Prodotto:\t\t{prod.num}\t{prod.den}")
    print(f"Divisione:\t\t{div.num}\t{div.den}")




if __name__ == '__main__':

    Test()
