import numpy as np
import math as m
import matplotlib.pyplot as pyplot
from LiSim import sim
from bresenham import bresenham
import matplotlib.pyplot as plt
from scipy.special import expit

from LiSim import sim
from map_utils.vector_math import rotation
from user_utils import plot

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
plt.style.use('classic')
norm_scale = 1000

dim = (20,20)
pos = (5,5)

logodd_occ = 0.9
logodd_free = 0.7

carte = np.zeros(dim)
carte[pos[0]][pos[1]] = 1000
lidar = sim.Lidar(dim=dim,pos=pos) #Initialize a lidar object
true_carte = lidar.carte
lidar.make_path() #make directory to save the examples
path = lidar.path 


measure = lidar.simulate(show=False,noise=False)


for i in range(len(measure)):

    occ = (np.matmul( rotation(measure[i][1]), [measure[i][0],0] ) + pos).astype(int)

    #If the value is out of range, do nothing here
    if (0<occ[0]<dim[0]) and (0<occ[1]<dim[1]):
        carte[occ[0]][occ[1]] += logodd_occ

    #Draw a line Lidar <-> Point, and register all points on the line as unoccupied (the lidar would have detected if not)
    points = np.array(list(bresenham(occ[0],occ[1],pos[0],pos[1])))
    for x,y in points:
        if (x!=occ[0] or y!=occ[1]) and (0<x<dim[0]) and (0<y<dim[1]):
            carte[x][y] -= logodd_free


scaled_carte = expit(carte*norm_scale)

lidar.plot_and_save_map_in(show=True)
plot.plot_and_save_map_out(scaled_carte,path,show=True)
confusion = plot.confusion_matrix(scaled_carte, true_carte,path)
