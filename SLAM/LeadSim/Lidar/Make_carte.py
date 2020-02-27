import matplotlib.pyplot as plt
import numpy as np
import sys
from bresenham import bresenham
np.set_printoptions(threshold=sys.maxsize)

dim = [10,10]
points = []
data=[]
carte = np.zeros((10,10))

def onclick(event):
    points.append((int(event.xdata), int(event.ydata)))

fig,ax = plt.subplots()
ax.set(xlim=(0, 10),ylim=(0, 10))
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

for i in range(0,len(points)-1):
    data.append(list(bresenham(points[i][0],points[i][1],points[i+1][0],points[i+1][1])))
    
data.append(list(bresenham(points[3][0],points[3][1],points[0][0],points[0][1])))

print(data)

for k in range(0,len(data)):
    for i in range(0,len(data[k])):
        carte[data[k][i][0]][data[k][i][1]] = 1

np.savetxt('te.txt', carte, delimiter=',') 
