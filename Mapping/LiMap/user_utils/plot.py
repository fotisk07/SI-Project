import numpy as np
import matplotlib.pyplot as plt
import os, sys, errno

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
plt.style.use('classic')

_basePath = "Example/default"

def setupPath(path="Example/default"):
    global _basePath
    _basePath = path
    try:
        os.mkdir(_basePath)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

# TODO: Slugification
def plotData(data, name, show=False, printa=False, save=True):
    global _basePath

    if printa==True:
        print(name+" is:\n", data)

    graph = plt.figure(name)
    plt.imshow(data)
    plt.colorbar()

    if save==True:
        graph.savefig(_basePath+"/"+name+".png")
    if show==True:
        graph.show()

    return graph
