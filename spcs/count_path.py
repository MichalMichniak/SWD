import numpy as np

def cum_count_path(woron_points,metrics = None):
    if metrics == None:
        metrics = lambda x,y: np.sqrt(np.dot(y-x, y-x))
    paths = [0]
    for i in range(1,len(woron_points)):
        paths.append(paths[i-1]+metrics(woron_points[i-1],woron_points[i]))
    return np.array(paths)
