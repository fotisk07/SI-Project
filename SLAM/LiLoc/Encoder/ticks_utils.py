import numpy as np

def ticks_to_dist(ticks,tourTick,startpos, wheel_radius=0.1):
    return (ticks*2*np.pi*wheel_radius)/tourTick + startpos

def ticks_to_v(dist, dt,startPos):
    return (dist-startPos)/dt
