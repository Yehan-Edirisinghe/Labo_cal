from scipy.stats import norm
from scipy.integrate import quad
import numpy as np
import es

'''
Use the Python scipy.stat.norm object to determine the area of a normal distribution
    of its tails outside the range included within an interval of 1, 2, 3, 4, 
    and 5 standard deviations around its mean
'''

def area(sample,t):

    m   = es.xMin(sample)
    M   = es.xMax(sample)
    mea = es.mean(sample)
    sigma = es.stdDeviation(sample)

    x = np.arange(m,M,0.1)
    func = lambda x : norm.pdf(x,mea,sigma)
    area = quad(func,-sigma*t,sigma*t)

    return area

if __name__ == '__main__':

    sample = es.file('eventi_gauss.txt')
    a = 1
    print("Area for", a, "standard deviations:\t",area(sample,a))