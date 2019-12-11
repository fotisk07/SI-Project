import numpy as np
import matplotlib.pyplot as plt
import os, sys, errno
import cv2
import seaborn as sns
import pandas as pd
from cv2 import VideoWriter, VideoWriter_fourcc
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

frames = []

plt.show(block=True)
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
def plotData(data, name,pos, show=False, printa=False, save=True,path=""):
    plt.style.use('ggplot')
    if path=="":
        path = _basePath
    if printa==True:
        print(name+" is:\n", data)

    data[pos[0]][pos[1]] = 1
    graph = plt.figure(name)
    plt.imshow(data,cmap='jet')
    plt.colorbar()

    if save==True:
        graph.savefig(path+"/"+name+".png")
    if show==True:
        plt.show()

    return graph

def plot_loss(loss,i, show=False, printa=False, save=True, path=""):
    plt.style.use('seaborn')
    if path=="":
        path = _basePath
    if printa==True:
        print(name+" is:\n", data)

    graph = plt.figure("Loss")
    x = np.arange(0,i,1)
    plt.plot(x,loss)
    plt.xlabel("Nombre de Tours")
    plt.ylabel("LoggLoss")
    if save==True:
        graph.savefig(path+"/"+"loss"+".png")
    if show==True:
        plt.show()

    return graph

def animate(image,center_coordinates,name):
    global frames
    radius = 20
    color = (255, 255, 255)
    thickness = 1
    image = (image/np.amax(image))*255
    image = cv2.applyColorMap(image.astype(np.uint8), cv2.COLORMAP_JET)
    image = cv2.circle(image, center_coordinates, 1, color, thickness)
    image = cv2.resize(image,(500,500))
    cv2.imshow(name, image)
    frames.append(image)
    cv2.waitKey(20)

def create_video(path):
    global frames
    if path=="":
        path = _basePath
    width = 500
    height = 500
    gifFps = 10
    fourcc = VideoWriter_fourcc(*'MP42')
    video = VideoWriter(path+'/Animation.avi', fourcc, float(gifFps), (width, height))
    for i in frames:
        video.write(i)
    video.release()
