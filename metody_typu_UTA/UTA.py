import numpy as np
from min_max_przedzial import min_max_przedzialik
from idealny_antyidealny import punkt_i_a
from funkcja_uzytecznosci import zwroc_f_u
from nowa_funkcja import nowa_funkcja

def UTA(A: np.ndarray, wartosci_u: np.ndarray , ilosc_przedzialow : np.ndarray):
    x = min_max_przedzialik(A,ilosc_przedzialow)
    print(x)
    a_b = zwroc_f_u(wartosci_u,x)
    lst = []
    for i in range(len(A)):
        lst.append(nowa_funkcja(a_b,x,A[i,:])) 
    return lst
    pass


if __name__ == '__main__':
    A = np.array(
        [[3.6,4,4399],[3.7,12,8199],[3.9,13,8299],[4.5,6,7299],[3.5,11,5399],[4.5,4,4549],[4.6,10,7699],[3.7,9.5,2699],[3.1,17,4049],[3.6,13,3200],[3.7,15,5699],[4.2,17,7399],[5.1,20,10499],[4.7,10,5099],[4.2,14,5099],[4.6,14,5099]]
    ,dtype=float)
    print(UTA(A,np.array([[0.34,0.18,0],[0.33,0.18,0],[0.33,0.28,0.14,0]]),np.array([2,2,3]))) 