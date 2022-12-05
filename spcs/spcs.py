from typing import List,Callable
from zdominowane import zdominowane
import numpy as np

def norm(A : List[List[float]], C :  List[List[float]]):
    A1=np.array(A)
    C1=np.array(C)
    normalizedA=(A1-np.min(A1))/(np.max(A1)-np.min(A1))
    normalizedC=(C1-np.min(C1))/(np.max(C1)-np.min(C1))
    return normalizedA,normalizedC

def SPCS(A : List[List[float]], C :  List[List[float]],min_max_criterial_funct : List[Callable[[np.ndarray],float]],metr = None):
    pass