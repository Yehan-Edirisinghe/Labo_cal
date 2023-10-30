from sys import exit
import numpy as np
from math import gcd


class Fraction:
    
    def __init__(self,num,den):
        
        
        if den == 0:
        	raise ValueError("Can't have 0 as denominator")
        if type(num) != int or type(den) != int:
        	raise TypeError("Numbers must be integers")
		
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
        print(f"{self.num}/{self.den}")

def Test():

    first = Fraction(2,5)
    second = Fraction(1,2)

    print("Prima frazione:")
    first.print()
    print("Seconda frazione:")
    second.print()
    
    somma   = first+second
    sott    = first-second
    prod    = first*second
    div     = first/second
	
    print("Somma:")
    somma.print()
    print("Sottrazione:")
    sott.print()
    print("Moltiplicazione:")
    prod.print()
    print("Divisione:")
    div.print()
    




if __name__ == '__main__':

    Test()
