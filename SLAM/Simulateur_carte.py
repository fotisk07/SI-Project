# Main program loop for LiSim simulation
from scipy.special import expit
import numpy as np
import matplotlib.pyplot as plt
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc
import time
import sys
from LeadSim.Lidar import sim
from LeadSim.Lidar import simResultProcess as prc
from LeadSim.Lidar import path_gen as gen
from LeadMap.map_utils import map
from LeadSim.Lidar.Plot import Carte_plot as cplot
from LeadSim.Lidar.Plot import Confidence as conf
import argparse

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

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
        Alexander Flamant
        Theodore Halley
        Fotios Kapotos
        Mateo Rivera
     """)
parser.add_argument("-d","--dimensions",
    nargs=2,
    help="""\
        This should be the x y size of the map.
    ex: "10 10"
    """,
    type=int
)
parser.add_argument("-p","--position",
    nargs=2,
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
parser.add_argument("-ani", "--animate",
    help="""\
        Add this option if you wish to display the mapping in an animated mode
    """,
    action="store_true"
)
parser.add_argument("-g", "--graphs",
    help="""\
        Add this option if you want to display the finished graphs and the loss evolution
    """,
    action="store_true"
)
parser.add_argument("-stats", "--stats",
    help="""\
        Add this option if you want to save a txt file with all the parameters
    """,
    action="store_true"
)
parser.add_argument("-video", "--video",
    help="""\
        Add this option if you want to save an avi file with the animation
    """,
    action="store_true"
)
parser.add_argument("-rl", "--relativeLoss",
    help="""\
        Add this option if you want to save an avi file with the animation
    """,
    action="store_true"
)
parser.add_argument("-tours", "--tours_number",type=int,
    help="""\
        Number of tours
    """,
    default=100000
)
args = parser.parse_args()
try:
    dim = tuple(args.dimensions)
    pos = tuple(args.position)
except:
    pass
isNoisy = args.noise
changeEx = args.save
animate = args.animate
graphs = args.graphs
stats = args.stats
video = args.video
relativeLoss = args.relativeLoss
tours_number = args.tours_number
norm_scale = 0.01 #Map Scaling variable
FPT = 1 #How many times the map will be update before plotted
logloss = [] #Logloss list for plotting



#Initialize and get base info from LiSim
try:
    lidar = sim.Lidar(dim=dim,pos=pos, uDist=3)
    print("Hey")
except:
    lidar = sim.Lidar()

true_carte = lidar.carte
carte = lidar.initialCarte


# Setup save file paths for the simulation
if changeEx:
    path = "Examples/dim="+str(dim)+"_pos=" +  str(lidar.pos)
    cplot.setuprootPath(path)
else:
    path = "Examples/default"
    cplot.setuprootPath()


start = time.time() #start the clock
for tours_count in range(1,tours_number+1):
    #Generate the data points where the measurements must be made
    measure_points =np.array(gen.measure_turn(lidar.pos, 1))
    # Simulate measurement
    simMeasure = lidar.simulate(points=measure_points,show=False,noise=isNoisy)
    #Update carte
    carte = map.processLidarData(simMeasure, carte, lidar.pos, lidar.dim, logodd_occ = 80 ,logodd_free = 20)
    if animate:
        #Convert carte in 0-1 format
        scaled_carte = expit(carte*norm_scale)
        #Animate
        cplot.animate(scaled_carte,lidar.pos,"Produced Carte")
        if cv2.waitKey(1) & 0xFF == ord('q'): break
        #Generate confusion matrix and logloss
        confusion = prc.genConfusionMatrix(scaled_carte, true_carte, lidar.pos)
        logloss.append(prc.smart_loss(lidar, confusion,False))
    else:
        scaled_carte = expit(carte*norm_scale)
        break

cv2.destroyAllWindows()
animation_time = time.time()-start # Measure running time
if animate==True: print("FPS:", tours_count/animation_time)
if animate==True: print("Loss:",logloss[-1])
print("Nombre de tours:",tours_count)
print("Confidence Score:",conf.confidence(scaled_carte))

#Plot the data
if graphs == True:
    confusion = prc.genConfusionMatrix(scaled_carte, true_carte,lidar.pos)
    cplot.plotData(confusion,"Confusion-Matrix",lidar.pos)
    cplot.plotData(true_carte,"Real-Map",lidar.pos)
    cplot.plotData(scaled_carte,"Produced-Map",lidar.pos)
    if animate == True:
        cplot.plot_loss(logloss,tours_count)
    else:
        print("Loss",prc.smart_loss(lidar, confusion,False))
    plt.show()

if stats == True:
    stats_for_nerds = {
    "Dimensions" : lidar.dim,
    "Position" : lidar.pos,
    "Noise" : isNoisy,
    "uPos": lidar.uPos,
    "uDist": lidar.uDist,
    "uTheta": lidar.uTheta,
    "Angle_step": lidar.angle_step,
    "Ray_step": lidar.ray_step ,
    "Norm Scale": norm_scale,
    "FPT": FPT,
    "Last logloss": logloss[-1],
    "Tours Count": tours_count,
    "FPS" :tours_count/animation_time,
    "Animation Runtime(s)": animation_time
    }

    f = open(path+"/stats for nerds.txt","w")
    f.write(str(stats_for_nerds) )
    f.close()

if video == True and animate==True:
    plot.create_video(path)
