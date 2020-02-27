import numpy as np
import math as m
import matplotlib.pyplot as plt
import os, sys

plt.style.use('classic')

class Lidar:
    '''Class that defines the Lidar object and comes with the simulation properties needed'''

    def __init__(self,dim=(50,50),angle_step=1, ray_step=1,pos=(25,25),uPos=2,uDist=2,uTheta=1.25):
        self.dim = dim
        self.angle_step = angle_step
        self.ray_step = ray_step
        self.carte = np.zeros(dim)
        self.pos = pos
        self.uPos = uPos
        self.uDist = uDist
        self.uTheta = uTheta

        #Map Boundaries and obstacle settings
        self.carte[0][:] = 1
        self.carte[:,0] = 1
        self.carte[dim[1]-1][:] = 1
        self.carte[:,dim[1]-1] = 1

        for i in range(15,25):
            self.carte[11][i] = 1

        for i in range(16,20):
            self.carte[i][i]=1


        #Create the reference initial working map for LiMap
        self.initialCarte = np.zeros(dim)



    def _noise(self, clean_data, dev, esp=0):
        '''Function that adds noise from a normal distribution to the data provided to mimic real world'''
        data = np.array(clean_data)
        noise = np.random.normal(esp,dev,clean_data.shape)
        return noise+clean_data

    def simulate(self, points, noise=True, show=False):
        '''Simulates data from one complete lidar rotation, the points parameter is
        a list representing a discretized version of the path and the laser orientation
        of the LiDAR over time '''

        simulated = []
        for i in range(len(points)-1):
            current_ray = 1
            theta = points[i][0][1]
            pos = points[i][0][0]
            while True:
                x_current = int(m.cos(m.radians(i))*current_ray)
                y_current = int(m.sin(m.radians(i))*current_ray)

                if self.carte[x_current+pos[0]][y_current+pos[1]] == 1:
                    simulated.append([current_ray, theta])
                    break
                current_ray += self.ray_step

        simulated = np.array(simulated)
        if noise == True:
            #Add noise to the data
            simulated[:,0] = self._noise(simulated[:,0], self.uDist)
            simulated[:,1] = self._noise(simulated[:,1], self.uTheta)


        return simulated
