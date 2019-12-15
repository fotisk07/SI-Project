import numpy as np

def ticks_to_dist(ticks,tourTick, wheel_radius=0.1):
    return (ticks*2*np.pi*wheel_radius)/tourTick

def ticks_to_v(dist, dt):
    return dist/dt
