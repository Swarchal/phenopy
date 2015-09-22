from numpy import dot
from math import sqrt, acos, pi

def theta0(a):
    
    """ Calculates the angle between a vector 'a' (tuple), and the origin
    in an anti-clockwise direction """
    
    origin = (1, 0)
    
    def norm_vec(x):
        norm_out = sqrt(dot(x, x))
        return norm_out
    
    theta = acos(dot(a, origin) / (norm_vec(a) * norm_vec(origin))) * 180 / pi
    
    if a[1] >= 0:
        print theta
    elif a[1] < 0:
        print 360 - theta
    