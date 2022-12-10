import numpy as np

def czy_w_obszarze(u,pkt1,pkt2):
    isTRUE=[]
    for i in range(len(u)):
        isTRUE.append(pkt1[i]<=u[i]<=pkt2[i] or pkt2[i]<=u[i]<=pkt1[i])
    for j in range(len(isTRUE)):
        if (isTRUE[j]==False):
            return False
    return True