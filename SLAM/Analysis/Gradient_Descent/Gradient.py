import numpy as np

def gradient(x,y,z):
    h=1
    try:
        dx_value = (z[x+h][y] - z[x][y])/h
        dy_value = (z[x][y+h] - z[x][y])/h
    except:
        dx_value = 0
        dy_value = 0
        
    return np.array([dx_value, dy_value])
