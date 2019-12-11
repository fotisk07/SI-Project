import numpy as np

def ticks_to_dist(ticks,tourTick, wheel_radius=1):
    return ticks/tourTick*2*pi*wheel_radius

def ticks_to_v(ticks, tourTick, wheel_radius=1, dt=1):
    omega = 2*pi*ticks/tourTick*dt
    return omega*wheel_radius
    
