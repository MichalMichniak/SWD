from typing import List,Callable
from zdominowane import zdominowane
import numpy as np
from woronoj_pkt import woronoj
from count_path import cum_count_path
from czy_w_obszarze import czy_w_obszarze
from costam import costam

def norm(A : List[List[float]], C :  List[List[float]]):
    A1=np.array(A)
    C1=np.array(C)
    normalizedA=(A1-np.min(A1))/(np.max(A1)-np.min(A1))
    normalizedC=(C1-np.min(C1))/(np.max(C1)-np.min(C1))
    return normalizedA,normalizedC

def SPCS(idealny : List[np.ndarray], antyidealny : List[np.ndarray], punkty : List[np.ndarray]):
    scoring = []
    for pkt in range(len(punkty)):
        scoring.append(0)
        for ide in range(len(idealny)):
            for anty in range(len(antyidealny)):
                minimal = np.inf
                d_path = 0
                w = czy_w_obszarze(pkt,ide,anty)
                if w == -1:
                    continue
                woron_point = woronoj(anty,ide)
                cum_path = cum_count_path(woron_point)
                for i in range(1,len(woron_point)):
                    d,metric = costam(woron_point[i-1],woron_point[i],punkty[pkt])
                    if d == -1:
                        continue
                    if minimal>metric:
                        minimal = metric
                        d_path = cum_path[i-1]+d
                ### sprawdzanie punktów woronoja
                for i in range(1,len(woron_point)):
                    metric = np.linalg.norm(punkty[pkt]-woron_point[i])
                    if minimal>metric:
                        minimal = metric
                        d_path = cum_path[i]
                ###
                scoring[pkt] += w*d_path
    return scoring
    pass


if __name__ == "__main__":
    SPCS(0,0,0)