import numpy as np
from random import gauss

class Gyro():

    def __init__(self,startTheta, startThetadot, thetadotdot):
        self.startTheta = startTheta
        self.startThetadot = startThetadot
        self.thetadotdot = thetadotdot

    def _noise(self,data,mu=0,std=5):
        return data + gauss(mu,std)

    def theta(self,t, noise=False):
        if noise:
            return self._noise(self.startTheta + self.startThetadot*t + 1/2*self.thetadotdot*(t**2))
        else:
            return self.startTheta + self.startThetadot*t + 1/2*self.thetadotdot*(t**2)

    def thetadot(self,t,noise=False):
        if noise:
            return self. _noise(self.thetadotdot*t + self.startThetadot)
        else:
            return self.thetadotdot*t + self.startThetadot
