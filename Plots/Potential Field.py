import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
plt.style.use('seaborn-white')
import numpy as np

res_x = 100
res_y = 100
start = [1,6]
ksi = 100

def f(x, y):
    print(x.shape)
    pos = np.array([x,y])
    print(pos.shape)
    #return ksi*np.linalg.norm(pos-start,axis=0)
    return np.sqrt(np.square(x-start[0])+np.square(y-start[1]))



x = np.linspace(0, 10, res_x)
y = np.linspace(0, 10, res_y)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
print(Z.shape)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
plt.show()
