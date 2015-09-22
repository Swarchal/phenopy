from numpy import dot
from math import sqrt, acos, pi

def theta(a, b):
    
    """ Calculates the angle between vectors 'a' and 'b' (tuples) """
    
    
    def norm_vec(x):
        norm_out = sqrt(dot(x, x))
        return norm_out
    
    theta = acos(dot(a, b) / (norm_vec(a) * norm_vec(b))) * 180 / pi
    
    print theta
    
