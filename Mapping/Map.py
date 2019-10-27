import numpy as np
import math as m
import matplotlib.pyplot as pyplot
from LiSim import sim
from bresenham import bresenham
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
plt.style.use('classic')
dim = (20,20)
pos = (2,5)
logodd_occ = 0.9
logodd_free = 0.7
norm_scale = 5
carte = np.zeros(dim)
carte[pos[0]][pos[1]] = 1000
lidar = sim.Lidar(dim=dim,pos=pos)
true_carte = lidar.give_carte()

lidar.make_path()

def sigmoid(X):
    '''Function to normalize the map obtained'''
    return 1 / (1 + np.exp(-X*norm_scale))

def confusion_matrix(obs,true,show=False,print=False,save=True):
    '''Function that saves and shows the confunsion matrix'''
    confusion_matrix = np.square(obs-true)

    if show==True:
        print("The confusion matrix is:\n", confusion_matrix)
    if save==True:
        conf = plt.figure("Confusion Matrix")
        plt.imshow(confusion_matrix)
        plt.colorbar()
        conf.savefig("Examples/"+lidar.path+"/Confusion_matrix.png")
    if print==True:
        conf.show()
    return confusion_matrix

def rotation(theta):
    '''Rotation Matrix for coordinate transformations'''
    return np.array([[np.cos(m.radians(theta)),-np.sin(m.radians(theta))],[np.sin(m.radians(theta)),np.cos(m.radians(theta))]])

def plot_produced_map(carte,show=False):
    produced = plt.figure("Output Map")
    plt.imshow(carte)
    plt.colorbar()
    produced.savefig("Examples/"+lidar.path+"/Produced_map.png")
    if show == True:
        produced.show()
        
def save_and_plot(plot=False):
    path = lidar.path
    np.savetxt("Examples/"+lidar.path+"/Produced_map.txt",carte,delimiter=',',fmt='%1.1f')
    lidar.save_carte()
    np.savetxt("Examples/"+lidar.path+"/Confusion_matrix.txt",confusion,delimiter=',',fmt='%1.1f')
    
    if plot==True:
        plt.show()


measure = lidar.simulate(show=False)
lidar.plot_map(show=False)

for i in range(360):

    occ = (np.matmul( rotation(measure[i][1]), [measure[i][0],0] ) + pos).astype(int)

    carte[occ[0]][occ[1]] += logodd_occ

    #Draw a line Lidar <-> Point, and register all points on the line as unoccupied (the lidar would have detected if not)
    points = np.array(list(bresenham(occ[0],occ[1],pos[0],pos[1])))
    for x,y in points:
        if x!=occ[0] or y!=occ[1]:
            carte[x][y] -= logodd_free


plot_produced_map(sigmoid(carte),show=False)
confusion = confusion_matrix(sigmoid(carte), true_carte)
save_and_plot(plot=True)  






































