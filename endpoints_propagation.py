"""
Code for endpoints propagation of intervals. A few warnings:

* The code is exponential in the number of interval inputs (2^n). So there is little point in vectorising the code. 
* Endpoints propagation is exact only for functions that are monotonic in the number of inputs. 

This propagation can be run independently from an interval arithemtic library. 

"""
import numpy as np
from typing import Callable

def a(x): return np.asarray(x,dtype=float)


def turn_to_mask(index:np.ndarray,dim=2):
    ''' Turn a vector of 0s and 1s e.g. (1,0,0,0,1) into a masking array [(0,1),(1,0),(1,0),(1,0),(0,1)].
    If dim > 2,  e.g. (2,0,1,0) the mask is [(0,0,1),(1,0,0),(0,1,0),(1,0,0)]. '''
    index = np.asarray(index,dtype=int)
    return np.asarray([index==j for j in range(dim)],dtype=bool)

def endpoints_propagation_2n(x:np.ndarray,f:Callable): # Computes the min and max of a monotonic function with endpoints propagation
    "x has shape (n,2)."
    n=x.shape[0]
    max_candidate=-np.Inf
    min_candidate=np.Inf
    for j in range(2**n):
        b = tuple([j//2**h-(j//2**(h+1))*2 for h in range(n)]) # tuple of 0s and 1s
        s = turn_to_mask(b).T
        new_f = f(*x[s])
        if new_f > max_candidate:
            max_candidate =  new_f
            max_corner = b
        if new_f < min_candidate:
            min_candidate =  new_f
            min_corner = b
    return min_candidate, max_candidate, min_corner, max_corner

