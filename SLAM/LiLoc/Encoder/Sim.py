import numpy as np
import math as m

class Encoder():

    def __init__(self,ticsTours,velocity,acceleration,startPos):
        self.ticsTours = ticsTours
        self.velocity = velocity
        self.acceleration = acceleration
        self.startPos = startPos
        self.wheelRadius = 0.1

    def getTicks(self,t):
        '''Assuming constant acceleration'''
        newPos = self.startPos + self.velocity*t + 1/2*self.acceleration*t**2
        tics = int(newPos / 2*m.pi*self.wheelRadius) * self.ticsTours
        return tics

    def distance(self,t):
        newPos = self.startPos + self.velocity*t + 1/2*self.acceleration*t^2
        return newPos
