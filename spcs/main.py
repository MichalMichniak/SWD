from typing import List,Callable
from zdominowane import zdominowane
from spcs import norm, SPCS
import numpy as np

if __name__ == '__main__':
    min_max = [np.max,np.min,np.min]
    Ide = np.array([[16,4000,10],[32,5000,25],[16,4000,20]])
    AIde = np.array([[8,5000,30],[16,7000,100],[32,10000,50]])
    badane = np.array([[16,8000,35],[32,8000,90],[8,4500,12]])
    print(SPCS(Ide,AIde,badane))