# Main program loop for LiSim simulation
from scipy.special import expit
import numpy as np
import matplotlib.pyplot as plt
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc
import time
import sys
from LiSim import sim
from LiSim import simResultProcess as prc
from LiSim import path_gen as gen
from LiMap.map_utils import map
from LiMap.user_utils import plot
import argparse

dim = [50,50]
pos= [0,0]

lidar = sim.Lidar(dim=dim, pos=pos)
true_carte = lidar.carte
carte = lidar.initialCarte
data=np.zeros((dim[0]*dim[1],3))


for j in range(0,dim[0]):
    occ = 0.01+j*0.02
    if j%2 == 0:
        print("I hate myself {}/{}".format(j/2,dim[0]/2))
    for i in range(0,dim[1]):
        free = 0.01+0.02*i
        for tours_count in range(1,11):
            #Generate the data points where the measurements must be made
            measure_points =np.array(gen.measure_turn(lidar.pos, 1))
            # Simulate measurement
            simMeasure = lidar.simulate(points=measure_points,show=False,noise=True)
            #Update carte
            carte = map.processLidarData(simMeasure, carte, lidar.pos, lidar.dim,occ,free)
            scaled_carte = expit(carte)
            confusion = prc.genConfusionMatrix(scaled_carte, true_carte,lidar.pos,False)
            loss = prc.loss(confusion,lidar.dim)
        data[dim[0]*j+i][:]=[occ,free,loss]
        if i % 10 ==0:
            print("You suck")

np.savetxt('Analysis/Loss_Points.txt', data, delimiter=',')
