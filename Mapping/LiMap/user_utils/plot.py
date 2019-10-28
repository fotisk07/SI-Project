import numpy as np
import matplotlib.pyplot as plt
import os, sys, errno

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
plt.style.use('classic')

def plot_and_save_map_out(carte,path,printa=False,show=False,save=True):
    '''Plots, saves the plot, prints and saves the txt numpy array of the produced map'''
    if printa==True:
        print("The produced map is:\n", carte)
    if save==True:
        produced = plt.figure("Output Map")
        plt.imshow(carte)
        plt.colorbar()
        produced.savefig("Examples/"+path+"/Produced_map.png")
        np.savetxt("Examples/"+path+"/Produced_map.txt",carte,delimiter=',',fmt='%1.1f')
    if show == True:
        produced.show()

def confusion_matrix(obs,true,path,show=False,printa=False,save=True):
    '''Plots, saves the plot, prints and saves the txt numpy array of the confusion matrix'''

    confusion_matrix = np.square(obs-true)

    if printa==True:
        print("The confusion matrix is:\n", confusion_matrix)
    if save==True:
        conf = plt.figure("Confusion Matrix")
        plt.imshow(confusion_matrix)
        plt.colorbar()
        conf.savefig("Examples/"+path+"/Confusion_matrix.png")
    if show==True:
        conf.show()

    return confusion_matrix

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
