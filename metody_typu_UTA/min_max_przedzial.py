import numpy as np
from idealny_antyidealny import punkt_i_a
def min_max_przedzialik(A : np.ndarray ,ilosc_przedzialow : np.ndarray):
    min_max = np.array([[np.min(A[:,i]),np.max(A[:,i])] for i in range(len(A[0,:]))])
    przedzialy = [np.linspace(min_max[i][0],min_max[i][1],ilosc_przedzialow[i]+1) for i in range(len(A[0,:]))]
    
    return przedzialy

if __name__ == '__main__':
    A = np.array(
        [[3.6,4,4399],[3.7,12,8199],[3.9,13,8299],[4.5,6,7299],[3.5,11,5399],[4.5,4,4549],[4.6,10,7699],[3.7,9.5,2699],[3.1,17,4049],[3.6,13,3200],[3.7,15,5699],[4.2,17,7399],[5.1,20,10499],[4.7,10,5099],[4.2,14,5099],[4.6,14,5099]]
    )
    func_max_min = [np.max,np.max,np.min]
    print(min_max_przedzialik(A,np.array([2,2,3])))
    print(punkt_i_a(func_max_min,A))


    