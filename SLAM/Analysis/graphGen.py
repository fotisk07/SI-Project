import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


data = np.loadtxt("Loss_Points.txt", delimiter=",")

shape = (25,25)


x = np.reshape(data[:,0], shape)
y = np.reshape(data[:,1], shape)
z = np.reshape(data[:,2], shape)
z[0][:] = 0.1
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, rstride=5, cstride=1,
                cmap='winter', edgecolor='none')
ax.set_title('Loss as a function of odd and free');
ax.set_xlabel('Free')
ax.set_ylabel("Occ")
ax.set_zlabel("Loss")
plt.savefig('Loss_Graph.png')


plt.show()
