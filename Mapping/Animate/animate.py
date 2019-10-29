#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
plt.style.use('classic')

init = np.zeros((10,10))
init[5][5]= 1
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
init = init.tolist()
plt.imshow(init)
plt.colorbar()
working=0

def animate(i):


    k=0
    data = open('frames.txt','r').read()
    lines = data.split('$')
    lines.pop()
    img = [init]
    for line in lines:
        image = np.fromstring(line, dtype=float, sep=',')

        image = image.reshape(10,10)
        a = image.tolist()
        img.append(a)
        k=len(img)-1

        print(img)


    ax1.clear()
    if i<k:
        plt.imshow(img[i])
    elif i>=k:
        plt.imshow(img[k-1])

    working=i



ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
