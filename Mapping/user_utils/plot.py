import numpy as np
import matplotlib.pyplot as plt

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
