from typing import List,Callable
from zdominowane import zdominowane
from spcs import norm, SPCS
import numpy as np

if __name__ == '__main__':
    min_max = [np.min,np.min]
    A = np.array([[1,1],
     [1,1],
     [1,1],
     [1,1],
     [1,1],
     [1,1]])
 
    K = np.array([[1, 200, 1, 3],
    [1, 1500, 7, 10]])

    print(norm(A,K))
    print(SPCS(A,K,min_max))
