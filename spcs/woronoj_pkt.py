import numpy as np
import matplotlib.pyplot as plt


def woronoj(pkt_1 : np.ndarray,pkt_2 : np.ndarray):
    N = len(pkt_1)
    pkt_2 = pkt_2-pkt_1
    pkt_1_temp = pkt_1
    pkt_1 = np.zeros(N)
    woronoj_points = [np.array([0,0,0]) for i in range(2*N)]
    woronoj_points[0] = pkt_1
    woronoj_points[-1] = pkt_2
    size_of_shift = np.abs(pkt_2 - pkt_1)/2
    sign_of_shift = np.sign(pkt_2 - pkt_1)
    mask_fixed = np.zeros(N)
    dimentions = np.ones(len(pkt_1))
    for i in range(1,N):
        woronoj_points[i] = woronoj_points[0] + np.min(size_of_shift) * sign_of_shift + mask_fixed
        woronoj_points[2*N-1-i] = woronoj_points[-1] + -1*np.min(size_of_shift) * sign_of_shift - mask_fixed
        idx = np.argmin(size_of_shift)
        mask_fixed[idx] = woronoj_points[i][idx]
        size_of_shift[idx] = np.inf
        sign_of_shift[idx] = 0
        dimentions[idx] = 0
    return np.array(woronoj_points) + pkt_1_temp

if __name__ == '__main__':
    x2 = np.array([1,0,3])
    x1 = np.array([1,2,-3])
    wor = woronoj(x1,x2)


    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    ax.plot3D(wor[:,0], wor[:,1], wor[:,2], 'green')
    plt.show()