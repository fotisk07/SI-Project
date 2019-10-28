import numpy as np
import math as m
import matplotlib.pyplot as plt
import os, sys
plt.style.use('classic')

class Lidar:
    '''Class that defines the Lidar object and comes with the simulation properties needed'''

    def __init__(self,dim=(15,15),angle_step=1, ray_step=1, mu=1,std=0.01,pos=(10,10)):
        self.dim = dim
        self.angle_step = angle_step
        self.ray_step = ray_step
        self.mu = mu
        self.std = std
        self.carte = np.zeros(dim)
        self.pos = pos
        self.carte[self.pos[0]][self.pos[1]] = 0.5
        self.path = "dim="+str(dim)+"_pos=" +  str(pos)

        #Map Boundaries and obstacle settings
        self.carte[0][:] = 1
        self.carte[:,0]=1
        self.carte[dim[0]-1][:]=1
        self.carte[:,dim[1]-1]=1

    def make_path(self):
        '''Create folder to save the different maps'''
        try:
            os.mkdir("Examples/"+self.path)
        except:
            pass
        return 

    def plot_and_save_map_in(self,show=False,printa=False,save=True):
        '''Plots, saves the plot, prints and saves the txt numpy array of the real map'''
        if printa== True:
            print("The real map is:\n", self.carte)
        real_map = plt.figure("Real Map")
        plt.imshow(self.carte)
        plt.colorbar()
        real_map.savefig("Examples/"+self.path+ "/Real_Map.png")
        np.savetxt("Examples/"+self.path+ "/Real_Map.txt", self.carte, delimiter=',',fmt='%1.1f')
        if show==True:
            real_map.show()


    def give_carte(self):
        return self.carte

    def _noise(self, clean_data, dev, esp=0):
        '''Function that adds noise from a normal distribution to the data provided to mimic real world'''
        data = np.array(clean_data)
        noise = np.random.normal(esp,dev,clean_data.shape)
        return noise+clean_data
    
    def simulate(self, show=False, uPos=2, uDist=2, uTheta=1.25):
        '''Simulates data from one complete lidar rotation'''
        data=[]
        if show == True:
            print(self.carte)
        for i in range(int(360/self.angle_step)):
            current_ray = 1
            theta = i
            while True:
                x_current = int(m.cos(m.radians(i))*current_ray)
                y_current = int(m.sin(m.radians(i))*current_ray)

                if self.carte[x_current+self.pos[0]][y_current+self.pos[1]] == 1:
                    data.append([current_ray, theta])
                    break
                current_ray += self.ray_step

        data = np.array(data)

        #Add noise to the data
        data[:,0] = self._noise(data[:,0], uDist)
        data[:,1] = self._noise(data[:,1], uTheta)


        return data
