from typing import List,Callable
from zdominowane import zdominowane
import numpy as np
from woronoj_pkt import woronoj
from count_path import cum_count_path


def norm(A : List[List[float]], C :  List[List[float]]):
    A1=np.array(A)
    C1=np.array(C)
    normalizedA=(A1-np.min(A1))/(np.max(A1)-np.min(A1))
    normalizedC=(C1-np.min(C1))/(np.max(C1)-np.min(C1))
    return normalizedA,normalizedC

def SPCS(idealny : List[np.ndarray], antyidealny : List[np.ndarray], punkty : List[np.ndarray]):
    woron_point = woronoj(np.array([1,2,3]),np.array([1,2,3]))
    print(cum_count_path(woron_point),woron_point)
    pass


if __name__ == "__main__":
    SPCS(0,0,0)