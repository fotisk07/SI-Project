import numpy as np
import math as m
import matplotlib.pyplot as plt
plt.style.use('classic')

class Lidar:
    '''Class that defines the Lidar object and comes with the simulation properties needed'''

    def __init__(self,dim=(15,15),angle_step=1, ray_step=1, mu=1,std=0.01,pos=np.array([10,10])):
        self.dim = dim
        self.angle_step = angle_step
        self.ray_step = ray_step
        self.mu = mu
        self.std = std
        self.carte = np.zeros(dim)
        self.pos = pos
        self.carte[self.pos[0]][self.pos[1]] = 0.5

        #Map Boundaries and obstacle settings
        self.carte[0][:] = 1
        self.carte[:,0]=1
        self.carte[dim[0]-1][:]=1
        self.carte[:,dim[1]-1]=1

        self.carte[15,:]=1

    def plot_map(self,show):
        plt.imshow(self.carte)
        plt.colorbar()
        plt.savefig("real_map.png")
        if show==True:
            plt.show()

    def save_carte(self):
        np.savetxt("carte.txt", self.carte, delimiter=',',fmt='%1.1f')

    def give_carte(self):
        return self.carte

    def noise(self, clean_data):
        '''Function that adds noise from a normal distribution to the data provided to mimic real world'''
        data = np.array(clean_data)
        noise = np.random.normal(self.mu,self.std,[int(360/self.angle_step),2])
        return noise+clean_data

    def simulate(self, show=False):
        '''Simulates data from one complete lidar rotation'''
        data=[]
        if show == True:
            print(self.carte)
        for i in range(int(360/self.angle_step)):
            current_ray = 1
            while True:
                x_current = int(m.cos(m.radians(i))*current_ray)
                y_current = int(m.sin(m.radians(i))*current_ray)

                if self.carte[x_current+self.pos[0]][y_current+self.pos[1]] == 1:
                    data.append((current_ray , i))
                    break
                current_ray += self.ray_step
        return np.array(data)
