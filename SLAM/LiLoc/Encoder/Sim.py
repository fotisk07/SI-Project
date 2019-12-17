import numpy as np
from random import gauss

class Encoder():

    def __init__(self,ticsTours,velocity,acceleration,startPos):
        self.ticsTours = ticsTours
        self.velocity = velocity
        self.acceleration = acceleration
        self.startPos = startPos
        self.wheelRadius = 0.1

    def _noise(self,data,mu=0,std=10):
        return int(data + gauss(mu,std))


    def getTicks(self,t,noise=True):
        '''Assuming constant acceleration'''
        newPos = self.distance(t)
        tics = (int((newPos-self.startPos) / (2*np.pi*self.wheelRadius))+1) * self.ticsTours
        if noise == True:
            tics = self._noise(tics)
        return tics

    def distance(self,t):
        newPos = self.startPos + self.velocity*t + 1/2*self.acceleration*t**2
        return newPos

    def vel(self,distance,t):
        try:
            v = (self.distance(t)-self.startPos) / t
        except:
            return 0
        return v
