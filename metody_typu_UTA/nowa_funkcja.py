import numpy as np


def nowa_funkcja(a_b,x,punkt_badany):
    suma = 0
    for i in range(len(punkt_badany)):
        j=0
        while punkt_badany[i]>x[i][j+1]:
            j+=1
        y = a_b[i][j][0]*punkt_badany[i] + a_b[i][j][1]
        suma += y
    return suma
            