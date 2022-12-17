import numpy as np
from typing import Callable

def punkt_i_a(func_max_min : Callable,A: np.ndarray):
    
    idealny = np.array([func_max_min[i](A[:,i]) for i in range(len(func_max_min))])
    antyidealny = np.array([(np.max(A[:,i]) if func_max_min[i] == np.min else np.min(A[:,i]) )for i in range(len(func_max_min))])
    return idealny, antyidealny