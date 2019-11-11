import numpy as np
import math as m
import matplotlib.pyplot as plt
import os, sys
from random import randint

plt.style.use('classic')

class Lidar:
    '''Class that defines the Lidar object and comes with the simulation properties needed'''

    def __init__(self,dim=(15,15),angle_step=1, ray_step=1,pos=(10,10)):
        self.dim = dim
        self.angle_step = angle_step
        self.ray_step = ray_step
        self.carte = np.zeros(dim)
        self.pos = pos
        self.carte[self.pos[0]][self.pos[1]] = 0.5
        self.true_carte = self.carte
        #Map Boundaries and obstacle settings
        self.carte[0][:] = 1
        self.carte[:,0]=1
        self.carte[dim[0]-1][:]=1
        self.carte[:,dim[1]-1]=1
        
        #Create the reference initial working map for LiMap
        self.initialCarte = np.zeros(dim)
        self.initialCarte[pos[0]][pos[1]] = 1000


    def _noise(self, clean_data, dev, esp=0):
        '''Function that adds noise from a normal distribution to the data provided to mimic real world'''
        data = np.array(clean_data)
        noise = np.random.normal(esp,dev,clean_data.shape)
        return noise+clean_data

    def crazy_random_obstacle(self,crazy_random_obs_prob):
        '''Rolls the dice and if its 1 it will introduced 2 random lines
        with thickness dim[0]/10 and dim[1]/10'''
        if randint(0, crazy_random_obs_prob)==1:
            print("hey")
            for i in range(randint(0,int(self.dim[0]-self.dim[0]/10)-1)):
                self.carte[i][:] = 1
            for i in range(randint(0,int(self.dim[1]-self.dim[1]/10)-1)):
                self.carte[:,i]=1
            

    def simulate(self, points, noise=False, show=False, uPos=2, uDist=2, uTheta=1.25,isCrazy=False,CrazyProb=6):
        '''Simulates data from one complete lidar rotation, the points parameter is
        a list representing a discretized version of the path and the laser orientation
        of the LiDAR over time '''
        
        simulated=[]
        if isCrazy==True:
            self.crazy_random_obstacle(CrazyProb)
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
            simulated[:,0] = self._noise(simulated[:,0], uDist)
            simulated[:,1] = self._noise(simulated[:,1], uTheta)

        self.carte = self.true_carte #Revert from the crazy carte
        return simulated
