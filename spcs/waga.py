from volume import volume
import numpy as np
def zwrot_wagi(Ide,Aide):
    waga=0
    for i in range(len(Ide)):
        waga=waga+volume(Ide[i],Aide[i])
    return waga