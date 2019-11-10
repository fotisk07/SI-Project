import numpy as np
import matplotlib.pyplot as plt
import os, sys, errno
import cv2
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
plt.style.use('classic')


_basePath = "Examples/default"

def setuprootPath(path="Examples/default"):
    global _basePath
    _basePath = path
    try:
        os.mkdir(_basePath)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

def setupPath(path="Examples/default"):
    try:
        os.mkdir(path)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

# TODO: Slugification
def plotData(data, name, show=False, printa=False, save=True,path="" ):
    if path=="":
        path = _basePath
    if printa==True:
        print(name+" is:\n", data)

    graph = plt.figure(name)
    plt.imshow(data)
    plt.colorbar()

    if save==True:
        graph.savefig(path+"/"+name+".png")
    if show==True:
        graph.show()

    return graph

def animate(image,center_coordinates):
    radius = 20
    color = (255, 0, 0)
    thickness = 2
    image = cv2.circle(image, center_coordinates, 1, color, thickness) 
    cv2.imshow("produced_carte", image)
    cv2.waitKey(20)
