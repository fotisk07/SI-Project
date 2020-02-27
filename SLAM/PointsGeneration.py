# Main program loop for LiSim simulation
from scipy.special import expit
import numpy as np
import matplotlib.pyplot as plt
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc
import time
import sys
from LeadSim import sim
from LiSim import simResultProcess as prc
from LiSim import path_gen as gen
from LiMap.map_utils import map
from LiMap.user_utils import plot
import argparse

points = [25,25]


lidar = sim.Lidar(dim=[40,40], pos=[20,20])
true_carte = lidar.carte
carte = lidar.initialCarte
data=np.zeros((points[0]*points[1],3))
free_start = 5
occ_start = 5
step = 5

for j in range(0,points[0]):
    occ = occ_start + j*step
    if j%2 == 0:
        print("Remaining {}/{}".format(j/2,points[0]/2))
    for i in range(0,points[1]):
        free = free_start + step*i
        for tours_count in range(1,11):
            #Generate the data points where the measurements must be made
            measure_points =np.array(gen.measure_turn(lidar.pos, 1))
            # Simulate measurement
            simMeasure = lidar.simulate(points=measure_points,show=False,noise=True)
            #Update carte
            carte = map.processLidarData(simMeasure, carte, lidar.pos, lidar.dim,occ,free)

        scaled_carte = expit(carte)
        confusion = prc.genConfusionMatrix(scaled_carte, true_carte,lidar.pos,False)
        loss = prc.smart_loss(lidar, confusion,False)
        data[points[0]*j+i][:]=[occ,free,loss]

plot.plotData(true_carte,"Real-Map",lidar.pos,show=True)

np.savetxt('Analysis/Loss_Points.txt', data, delimiter=',')
np.savetxt('Analysis/Gradient_Descent/Loss_Points.txt', data, delimiter=',')
