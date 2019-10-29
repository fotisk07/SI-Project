import numpy as np

def genConfusionMatrix(obs, true):
    return np.square(obs-true)
