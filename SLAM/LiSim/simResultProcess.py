import numpy as np
from sklearn.metrics import log_loss
import math
from scipy.special import expit

def genConfusionMatrix(obs, true, pos, rl=False):
    conf = 4*np.square(obs-true)
    if rl==False:
        return conf
    else:
        weights = np.ones(np.shape(obs))
        for i in np.arange(0,obs.shape[0]):
            for j in np.arange(0,obs.shape[1]):
                if (i==pos[0] and j==pos[1]) or (j==pos[0] and i==pos[1]):
                    weights[i][j] = 1
                else:
                    weights[i][j] = 1/math.sqrt((i-pos[0])**2+(j-pos[1])**2)*10

        return np.multiply(weights,conf)

def loss(conf,dim):
    return (np.sum(conf)/(dim[0]*dim[1]))
