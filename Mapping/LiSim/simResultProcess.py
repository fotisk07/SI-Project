import numpy as np
from sklearn.metrics import log_loss

def genConfusionMatrix(obs, true):
    return 4*np.square(obs-true)

def loss(conf,dim):
    return (np.sum(conf)/(dim[0]*dim[1]))
