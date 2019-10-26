import numpy as np
import math as m
import matplotlib.pyplot as pyplot
from LiSim import sim
from bresenham import bresenham

def rotation(theta):
    return np.array([[np.cos(m.radians(theta)),-np.sin(m.radians(theta))],[np.sin(m.radians(theta)),np.cos(m.radians(theta))]])

dim = (10,10)
pos = np.array([5,5])
logodd_occ = 0.9
logodd_free = 0.7
carte = np.zeros(dim)
carte[5][5] = 1000
lidar = sim.Lidar(dim=dim,pos=pos)
measure = lidar.simulate(show=True)

for i in range(360):

    occ = (np.matmul( rotation(measure[i][1]), [measure[i][0],0] ) + pos).astype(int)

    carte[occ[0]][occ[1]] += logodd_occ

    #Draw a line Lidar <-> Point, and register all points on the line as unoccupied (the lidar would have detected if not)
    points = np.array(list(bresenham(occ[0],occ[1],pos[0],pos[1])))
    for x,y in points:
        if x!=occ[0] or y!=occ[1]:
            carte[x][y] -= logodd_free

print(carte)
np.savetxt("produced_map.txt",carte,delimiter=',',fmt='%1.4e')
lidar.save_carte()
