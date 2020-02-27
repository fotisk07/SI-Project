import numpy as np

def confidence(carte):
    uncertainty = np.absolute(carte-0.5)
    return np.sum(uncertainty)/uncertainty.size
