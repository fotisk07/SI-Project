import numpy as np
import Gradient as math
import random

data = np.loadtxt("Loss_Points.txt", delimiter=",")
shape = (25,25)

x = np.reshape(data[:,0], shape)
y = np.reshape(data[:,1], shape)
z = np.reshape(data[:,2], shape)
z[0][:] = 0.1
z[:,0] = 0.1
dmin_coord = np.zeros(2)
min_coord = np.array([random.randint(0,shape[0]-2),random.randint(0,shape[0]-2)])
gamma = 0.1
alpha = 0.1
print("Start Cords:",min_coord)
for i in range(200):
    dmin_coord = alpha*dmin_coord - gamma * math.gradient(min_coord[0],min_coord[1],z)
    min_coord =  min_coord + dmin_coord
    min_coord = min_coord.astype(int)
    '''
    if i%10 == 0:
        print("Gradient:",math.gradient(min_coord[0],min_coord[1],z))
        print("Coords:", min_coord)
    '''

print("Final Coords:", min_coord)
print("X value",x[min_coord[0]][0])
print("Y value",y[min_coord[1]][0])

print("Min Loss:",z[min_coord[0]][min_coord[1]])
print("Real min loss:", np.unravel_index(np.argmin(z, axis=None), z.shape))
