import numpy as np

def volume(pkt1,pkt2):
    l=[]
    for j in range(len(pkt1)):
        if pkt2[j]>pkt1[j]:
            l.append(pkt2[j]-pkt1[j])
        else:
            l.append(pkt1[j]-pkt2[j])
    V=1
    for i in range(len(l)):
        V=V*l[i]
    return V
