import numpy as np
import matplotlib.pyplot as plt
def costam(w1:np.ndarray,w2: np.ndarray,w3: np.ndarray):
    w21=w2-w1
    w21_norm= w21/np.linalg.norm(w21)
    w3_p=w3-w1
    dot_p=np.dot(w21_norm,w3_p)
    new=dot_p*w21_norm
    if np.linalg.norm(w21)>np.linalg.norm(new):
        return np.linalg.norm(new), np.linalg.norm(w3_p - new)
    return -1,-1




if __name__ == '__main__':
    x1 = np.array([0,0,0])
    x2 = np.array([2,2,2])
    u = np.array([0.5,1,1])
    x = (x2-x1)/np.linalg.norm(x2-x1)
    norm,_ = costam(x1,x2,u)
    if norm == -1:
        print("PaconAAAAAAAAAAA")
    rzut = x1 + x*norm
    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    ax.scatter3D(x1[0], x1[1], x1[2], color = "#88c999")
    ax.scatter3D(x2[0], x2[1], x2[2], color = "#88c999")
    ax.plot3D(np.array([x1[0],x2[0]]), np.array([x1[1],x2[1]]), np.array([x1[2],x2[2]]), 'green')
    ax.scatter3D(u[0], u[1], u[2], color = "#FF1233")
    ax.scatter3D(rzut[0], rzut[1], rzut[2], color = "#0000FF")
    plt.show()