from iminuit import Minuit
from iminuit.cost import LeastSquares,UnbinnedNLL,BinnedNLL

def fit(cost,*args,**kwargs):

    my_minuit = Minuit(cost,*args,**kwargs)
    my_minuit.migrad()
    my_minuit.hesse()
    return my_minuit

