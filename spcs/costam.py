import numpy as np
def costam(w1:np.ndarray,w2: np.ndarray,w3: np.ndarray):
    w21=w2-w1
    w21_norm= w21/np.linalg.norm(w21)
    w3_p=w3-w1
    dot_p=np.dot(w21_norm,w3_p)
    new=dot_p*w3_p
    if np.linalg.norm(w21)>np.linalg.norm(new):
        return np.linalg.norm(new)
