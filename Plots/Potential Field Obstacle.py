import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
obs1=[4,5]
obs2 = [1,2]
d0 = 5
res_x = 100
res_y = 100
start = [1,6]
def ro(x,y):
    return min(np.sqrt(np.square(x-obs[0])+np.square(y-obs[1]))

def fr(x,y):
        return 10*np.square((1/ro(x,y))-1/d0)
def fp(x, y):
    pos = np.array([x,y])
    #return ksi*np.linalg.norm(pos-start,axis=0)
    return 100*np.sqrt(np.square(x-start[0])+np.square(y-start[1]))

def f(x,y):
    return fr(x,y)+fp(x,y)

x = np.linspace(0, 10, res_x)
y = np.linspace(0, 10, res_y)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
plt.show()

