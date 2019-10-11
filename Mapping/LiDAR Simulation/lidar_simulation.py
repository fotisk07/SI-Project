import numpy as np
import math as m
dim = (10,10)
carte = np.zeros(dim)
pos = np.array([5,5])
carte[pos[0]][pos[1]] = 0.5
carte[0][:]=1
carte[:,0]=1
carte[9][:]=1
carte[:,9]=1
angle_step = 1
ray_step = 1
mu = 0
std = 0.01
data = []

def noise(clean_data):
    data = np.array(clean_data)
    noise = np.random.normal(mu,std,[int(360/angle_step),2])
    return noise+clean_data
    

print(carte)
for i in range(int(360/angle_step)):
    current_ray = 1 
    while True:
        x_current = int(m.cos(m.radians(i))*current_ray)
        y_current = int(m.sin(m.radians(i))*current_ray)
        #print(x_current+pos[0],y_current+pos[1])
        #print(carte[x_current+pos[0]][y_current+pos[1]])
        try:
            if carte[x_current+pos[0]][y_current+pos[1]] == 1:
                data.append((current_ray , i))
                break
            current_ray += ray_step
        except:
                data.append((current_ray , i))
                break
            
print(data)
