import numpy as np
from sklearn.metrics import log_loss

def genConfusionMatrix(obs, true):
    return 4*np.square(obs-true)
def genConfWeightedMatrix(obs, true):
    weights = np.ones(np.shape(obs))
    for i in arange(0,np.shape(obs[0][:])):
        for j in arange(0,np.shape(obs[:,0])):
            weights[i][j] = log(1/(i^2+j^2))

    return np.dot(weights,genConfusionMatrix(obs,true))

def loss(conf,dim):
    return (np.sum(conf)/(dim[0]*dim[1]))
