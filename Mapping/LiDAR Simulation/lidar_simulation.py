import numpy as np
import math as m
#Init variables
dim = (15,15)
angle_step = 1
ray_step = 1
mu = 0
std = 0.01
data = []
carte = np.zeros(dim)
pos = np.array([10,10])
carte[pos[0]][pos[1]] = 0.5

#Map Boundaries and obstacle settings
carte[0][:] = 1
carte[:,0]=1
carte[dim[0]-1][:]=1
carte[:,dim[1]-1]=1

carte[3][:]=1


def noise(clean_data):
    data = np.array(clean_data)
    noise = np.random.normal(mu,std,[int(360/angle_step),2])
    return noise+clean_data

def simulate(show=False):
    if show == False:
        print(carte)
    for i in range(int(360/angle_step)):
        current_ray = 1 
        while True:
            x_current = int(m.cos(m.radians(i))*current_ray)
            y_current = int(m.sin(m.radians(i))*current_ray)
            try:
                if carte[x_current+pos[0]][y_current+pos[1]] == 1:
                    data.append((current_ray , i))
                    break
                current_ray += ray_step
            except:
                    data.append((current_ray , i))
                    break
    return data
            
def save_to_csv(data,name,path):
   np.save((str(path)+str(name)),data)





    
    

