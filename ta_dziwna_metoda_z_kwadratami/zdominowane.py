import numpy as np
from typing import Callable,List
def zdominowane(decision_matrix : np.ndarray, bounds : np.ndarray,min_max_criterial_funct : List[Callable[[np.ndarray],float]]):
    decision_matrix_copy = decision_matrix.copy()
    decision_matrix = decision_matrix[:,:]
    bounds = bounds[:,:]
    lst = []
    lst2 = []
    for i in range(len(decision_matrix)):
        if ((bounds[0]<=decision_matrix[i,:]).all() and (decision_matrix[i,:]<=bounds[1]).all()):
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
    for i in range(len(decision_matrix[0][:])):
        for j in range(len(decision_matrix[:][0])):
            if decision_matrix_copy[i][j] not in (np.array(lstnzd)).any():
                lstzd.append(decision_matrix_copy[i][j])
    return  np.array(lstzd),np.array(lstnzd)

if __name__=='__main__':
    min_max_crit = [np.min,np.min]
    A = np.array([[4,4],[5,4],[-2,0],[0,1],[2,1],[1,-3],[4,1],[3,2],[3,3],[3,-1],[-1,1],[0,-1],[4,-2],[-1,3]])
    K = np.array([[-np.inf,-np.inf],[np.inf,np.inf]])
    print(zdominowane(A,K,min_max_crit))