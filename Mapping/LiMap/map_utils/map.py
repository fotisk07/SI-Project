import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.special import expit
from skimage.draw import line

from LiSim import sim
from LiMap.map_utils.vector_math import rotation
from LiMap.user_utils import plot

logodd_occ = 0.9
logodd_free = 0.7

# TODO:  pos and dim parameters are temporary, should be extracted from measure and previous_map in future versions
def processLidarData(measure, previous_map, position, dim):
    global logodd_occ
    global logodd_free

    for i in range(len(measure)):

        occ = (np.matmul( rotation(measure[i][1]), [measure[i][0],0] ) + position).astype(int)

        #Take care of boundaries
        if occ[0]<0:
            occ[0] = 0
        if occ[1]<0:
            occ[1] = 0
        if occ[0]>=dim[0]:
            occ[0] = dim[0]-1
        if occ[1]>=dim[1]:
            occ[1] = dim[1]-1

        previous_map[occ[0]][occ[1]] += logodd_occ

        #Draw a line Lidar <-> Point, and register all points on the line as unoccupied (the lidar would have detected if not)
        rr, cc = line(occ[0],occ[1],position[0],position[1])
        for i in range(len(rr)):
            x = rr[i]
            y = cc[i]
            if (x!=occ[0] or y!=occ[1]) and (0<x<dim[0]) and (0<y<dim[1]):
                previous_map[x][y] -= logodd_free

    return previous_map #Is now modified as 'new map'
