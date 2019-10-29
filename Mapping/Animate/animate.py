#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig = plt.figure()



def animate(i):
    data = open('produced_map.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []
   
    for line in lines:
        print(line)
        image = np.fromstring(line, dtype=float)
        
    ax1.clear()
    plt.imshow(image)
    plt.colorbar()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Live graph with matplotlib')	
	
    
ani = animation.FuncAnimation(fig, animate, interval=1000) 
plt.show()
