# Main program loop for LiSim simulation
from scipy.special import expit
import numpy as np
import matplotlib.pyplot as plt

from LiSim import sim
from LiSim import simResultProcess as prc
from LiSim import path_gen as gen
from LiMap.map_utils import map
from LiMap.user_utils import plot

parser = parse.ArgumentParser(
    description=''' \
    A program that simulates LiDAR measurements
    ---------------------------------------------------
        The simulated measurements are then processed.
        The program uses the LiMap utility for mapping
    and the LiSim (which is dependent on LiMap) for all
    simulations purposes.
        ''',

    formatter_class=parse.RawDescriptionHelpFormatter,
    epilog="""\
    ---------------------------------------------------
        This software is released under the MIT license
    (more details in LICENSE.md)

        Initial work:
            Fotios Kapotos
            Alexander Flamant
            Mateo Rivera
     """)
parser.add_argument("dimensions",
    nargs=2,
    help="""\
        This should be the x y size of the map.
    ex: "10 10"
    """,
    type=int
)

parser.add_argument("position",
    nargs=2,
    help="""\
        This should be the starting x y coordinates of
    the LiDAR separated with a space. ex: "5 5"
    """,
    type=int
)

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
plt.style.use('classic')

dim = tuple(parser.dimensions)
pos = tuple(parser.position)

norm_scale = 5

#Initialize and get base info from LiSim
lidar = sim.Lidar(dim=dim,pos=pos)
true_carte = lidar.carte
carte = lidar.initialCarte


# Setup save file paths for the simulation
path = "dim="+str(dim)+"_pos=" +  str(pos)
# lidar.make_path()
plot.setupPath("Examples/"+path)

#Generate the data points where the measurements must be made
measure_points = gen.measure_turn(pos, 1)

# Simulate measurement and feed them into LiMap
simMeasure = lidar.simulate(data=measure_points,show=False,noise=False)
carte = map.processLidarData(simMeasure, carte, pos, dim)


#Process the data
scaled_carte = expit(carte*norm_scale)
confusion = prc.genConfusionMatrix(scaled_carte, true_carte)

#Plot the data, old functions in comment
plot.plotData(confusion, "Confusion-Matrix")
plot.plotData(true_carte, "Real-Map")
plot.plotData(scaled_carte, "Produced-Map")

plt.show()
