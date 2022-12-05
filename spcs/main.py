from typing import List,Callable
from zdominowane import zdominowane
from spcs import norm, SPCS
import numpy as np

if __name__ == '__main__':
    min_max = [np.min,np.min]
    A = np.array([[1,1,700,  2, 6],
     [1,1, 250,  2, 4],
     [1,1, 1200, 6, 9],
     [1,1, 880,  4, 9],
     [1,1, 450,  3, 8],
     [1,1, 1500, 2, 3]])
 
    K = np.array([[1, 200, 1, 3],
    [1, 1500, 7, 10]])

    print(norm(A,K))
