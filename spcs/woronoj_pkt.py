import numpy as np

def woronoj(pkt_1 : np.ndarray,pkt_2 : np.ndarray):
    N = len(pkt_1)
    size_of_shift = np.abs(pkt_2 - pkt_1)/2
    size_of_shift = np.abs(pkt_2 - pkt_1)/2
    axis = [True for i in range(N)]
    for i in range(N):

