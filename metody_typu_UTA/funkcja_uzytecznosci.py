import numpy as np

def zwroc_f_u(y_u_params, x_u_params):
    f = []
    for i in range(len(y_u_params)):
        a_b = []
        for j in range(len(y_u_params[i][1:])):
            a = (y_u_params[i][j-1]-y_u_params[i][j])/(x_u_params[i][j-1]-x_u_params[i][j])
            a_b.append([a,y_u_params[i][j-1]-a*x_u_params[i][j-1]])
        f.append(a_b)
    return f
