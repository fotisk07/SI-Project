import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


data = np.loadtxt("Loss_Points.txt", delimiter=",")

x = np.reshape(data[:,0], (50, 50))
y = np.reshape(data[:,1], (50, 50))
z = np.reshape(data[:,2], (50, 50))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')
ax.set_title('Loss as a function of odd and free');
ax.set_xlabel('Free')
ax.set_ylabel("Occ")
ax.set_zlabel("Loss")
plt.savefig('Loss_Graph.png')
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)


plt.show()
