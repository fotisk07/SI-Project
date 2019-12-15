import numpy as np

class Encoder():

    def __init__(self,ticsTours,velocity,acceleration,startPos):
        self.ticsTours = ticsTours
        self.velocity = velocity
        self.acceleration = acceleration
        self.startPos = startPos
        self.wheelRadius = 0.1

    def getTicks(self,t):
        '''Assuming constant acceleration'''
        newPos = self.distance(t)
        tics = (int((newPos-self.startPos) / (2*np.pi*self.wheelRadius))+1) * self.ticsTours
        return tics

    def distance(self,t):
        newPos = self.startPos + self.velocity*t + 1/2*self.acceleration*t**2

        return newPos
