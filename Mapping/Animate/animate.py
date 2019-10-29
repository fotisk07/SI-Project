#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
plt.style.use('classic')

init = np.zeros((10,10))
init[5][5]= 1
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.imshow(init)
plt.colorbar()


def animate(i):
    data = open('frames.txt','r').read()
    lines = data.split('$')
    lines.pop()
    img = []
    for line in lines:
        image = np.fromstring(line, dtype=float, sep=',')

        image = image.reshape(10,10)
        a = image.tolist()
        img.append(a)
        print("\n\n",img)



    ax1.clear()
    plt.imshow(img[i])
    plt.title('Live graph with matplotlib')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
