# Main program loop for LiSim simulation
from scipy.special import expit
import numpy as np
import matplotlib.pyplot as plt

from LiSim import sim
from LiSim import simResultProcess as prc
from LiMap.map_utils import map
from LiMap.user_utils import plot
from LiMap.user_utils import frames

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
plt.style.use('classic')

dim = (10,10)
pos = (5,5)
norm_scale = 5
turns = 10

#Initialize and get base info from LiSim
lidar = sim.Lidar(dim=dim,pos=pos)
true_carte = lidar.carte
carte = lidar.initialCarte
frames.make_frame(carte)

# Setup save file paths for the simulation
path = "Examples/dim="+str(dim)+"_pos=" +  str(pos)
# lidar.make_path()
plot.setupPath(path)

#Setup save file paths for the animation
animate_path = "Animate/dim="+str(dim)+"_pos=" +  str(pos)
plot.setupPath(animate_path)
open('Animate/frames.txt', 'w+').close()
open('produced_map.txt', 'w+').close()
input()

for i in range(turns):
    # Simulate measurement and feed them into LiMap
    simMeasure = lidar.simulate(show=False,noise=True,uPos=10)
    carte = map.processLidarData(simMeasure, carte, pos, dim)
    frames.make_frame(expit(carte))
    #plot.plotData(expit(carte), "Produced-Map{}".format(i),animate_path)

#Process the data
scaled_carte = expit(carte*norm_scale)
confusion = prc.genConfusionMatrix(scaled_carte, true_carte)

#Plot the data, old functions in comment
plot.plotData(confusion, "Confusion-Matrix",path)
plot.plotData(true_carte, "Real-Map",path)
plot.plotData(scaled_carte, "Produced-Map",path)
