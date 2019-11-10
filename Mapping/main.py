# Main program loop for LiSim simulation
from scipy.special import expit
import numpy as np
import matplotlib.pyplot as plt

from LiSim import sim
from LiSim import simResultProcess as prc
from LiSim import path_gen as gen
from LiMap.map_utils import map
from LiMap.user_utils import plot
import argparse

parser = argparse.ArgumentParser(
    description=''' \
    A program that simulates LiDAR measurements
    ---------------------------------------------------
        The simulated measurements are then processed.
        The program uses the LiMap utility for mapping
    and the LiSim (which is dependent on LiMap) for all
    simulations purposes.
        ''',

    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""\
    ---------------------------------------------------
        This software is released under the MIT license
    (more details in LICENSE.md)

        Initial work:
            Fotios Kapotos
            Alexander Flamant
            Mateo Rivera
     """)
parser.add_argument("-d","--dimensions",
    nargs=2,
    help="""\
        This should be the x y size of the map.
    ex: "10 10"
    """,
    required=True,
    type=int
)

parser.add_argument("-p","--position",
    nargs=2,
    required=True,
    help="""\
        This should be the starting x y coordinates of
    the LiDAR separated with a space. ex: "5 5"
    """,
    type=int
)

parser.add_argument("-n", "--noise",
    help="""\
        Add this option if you wish to add noise to the
    simulated data.
    """,
    action="store_true"
)
parser.add_argument("-s", "--save",
    help="""\
        Add this option if you wish to save your files in a dedicated folder in
        examples or just the default
    """,
    action="store_true"
)

args = parser.parse_args()

dim = tuple(args.dimensions)
pos = tuple(args.position)
isNoisy = args.noise
changeEx = args.save

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
plt.style.use('classic')


norm_scale = 0.002 #Map Scaling variable
FPT = 5 #How many times the map will be update before plotted
#Initialize and get base info from LiSim
lidar = sim.Lidar(dim=dim,pos=pos)
true_carte = lidar.carte
carte = lidar.initialCarte


# Setup save file paths for the simulation
if changeEx:
    path = "Examples/dim="+str(dim)+"_pos=" +  str(pos)
    plot.setuprootPath(path)
else:
    plot.setuprootPath()

i=0
while True:
    #Generate the data points where the measurements must be made
    measure_points =np.array(gen.measure_turn(pos, 1))

    # Simulate measurement and feed them into LiMap
    simMeasure = lidar.simulate(points=measure_points,show=False,noise=isNoisy)
    carte = map.processLidarData(simMeasure, carte, pos, dim)

    if i%FPT:
        plot.animate(expit(carte),pos)

    i+=1


#Process the data
scaled_carte = expit(carte*norm_scale)
confusion = prc.genConfusionMatrix(scaled_carte, true_carte)

#Plot the data, old functions in comment
plot.plotData(confusion, "Confusion-Matrix")
plot.plotData(true_carte, "Real-Map")
plot.plotData(scaled_carte, "Produced-Map")

plt.show()
