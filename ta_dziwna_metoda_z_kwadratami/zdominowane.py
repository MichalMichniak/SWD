import numpy as np
from typing import Callable,List
def zdominowane(decision_matrix : np.ndarray, min_max_criterial_funct : List[Callable[[np.ndarray],float]]):
    decision_matrix_copy = decision_matrix.copy()
    decision_matrix = decision_matrix[:,:]
    lst = []
    lst2 = []
    for i in range(len(decision_matrix)):
        lst.append(list(decision_matrix[i,:]))
        lst2.append(list(decision_matrix_copy[i,:]))
    decision_matrix = np.array(lst)
    decision_matrix_copy = np.array(lst2)
    lstzd = []
    lstnzd = []
    for i in range(len(decision_matrix)):
        for j in range(len(decision_matrix)):
            if i == j:
                continue
            temp = np.array([decision_matrix[i,k]<decision_matrix[j,k] if min_max_criterial_funct[k] == np.min else decision_matrix[i,k]>decision_matrix[j,k]  for k in range(len(decision_matrix[0]))])
            if temp.any():
                pass
            else:
                break
        else:
            lstnzd.append(list(decision_matrix_copy[i]))
    lst_copy=lst.copy()
    for i in range(len(lst_copy)):
            if lst_copy[i] not in lstnzd:
                lstzd.append(lst_copy[i])
    return  np.array(lstzd),np.array(lstnzd)

if __name__=='__main__':
    min_max_crit = [np.min,np.min]
    A = np.array([[4,4],[5,4],[-2,0],[0,1],[2,1],[1,-3],[4,1],[3,2],[3,3],[3,-1],[-1,1],[0,-1],[4,-2],[-1,3]])
    print(zdominowane(A,min_max_crit))