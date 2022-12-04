from typing import List
from zdominowane import zdominowane
import numpy as np

def wage(a0 : List[float],a1: List[float]):
    v = 1
    for n,i in enumerate(a0):
        v *= np.abs(a1[n] - i)
    return v

def metric(a : List[float],b : List[float]):
    d = np.dot(np.array(a)-np.array(b),np.array(a)-np.array(b))
    return np.sqrt(d)

def RSM(A : List[List[float]], C :  List[List[float]],metr = None):
    """
    RSM metoda zbiorów odniesienia

    args:
        A - zbiór punktów odniesienia
        B - zbiór punktów dopószczalnych

    return
        punkty skoringowe zbioru B
    """
    if metr == None:
        metr = metric
    try:
        A0,rest = zdominowane(A)
        A1,rest = zdominowane(rest)
    except:
        pass
    ## testy
    A0 = [[1,1],[2,2],[0,0]]
    A1 = [[2,3],[-1,1],[1,3]]
    ## koniec testów
    if len(A1) == 0:
        return "error"
    wages = np.zeros([len(A0),len(A1)])
    for i in range(len(wages)):
        for j in range(len(wages[0])):
            wages[i,j] = wage(A0[i],A1[j])
    ## Normalization
    wages = wages/np.sum(wages)
    lst_skoring = []
    for i in range(len(C)):
        lst_skoring.append(0)
        for j in range(len(wages)):
            for k in range(len(wages[0])):
                lst_skoring[i] += wages[j,k] * metr(C[i],A0[k])/(metr(C[i],A0[k])+metr(C[i],A1[j]))
    return lst_skoring

if __name__ == '__main__':
    A = [[2,3],[-1,1],[1,3],[1,1],[2,2],[0,0]]
    B = [[3,4],[5,1],[1,2],[3,3]]
    print(RSM([],B))