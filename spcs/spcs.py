from typing import List,Callable
from zdominowane import zdominowane
import numpy as np


def SPCS(A : List[List[float]], C :  List[List[float]],min_max_criterial_funct : List[Callable[[np.ndarray],float]],metr = None):
    k=len(A[0])
    d=[]
    for i in range(1,k+1):
        d[i]=()/2