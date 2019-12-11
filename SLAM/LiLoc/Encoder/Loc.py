import numpy as np
import Sim as sim
import math


data = [0,1,2,5,7,10,15]
ticksTours = 10
enc = sim.Encoder(ticksTours,5,0,0)
t = 10
dt = 1
X = 0

for i in range(0,t,dt):
    ticks = enc.getTicks(t)
    X = (ticks/10) * 0.1*2*math.pi

print(X)
