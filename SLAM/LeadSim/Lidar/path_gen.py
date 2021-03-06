from enum import Enum
import numpy as np

def rotation(theta):
    '''Rotation Matrix for coordinate transformations'''
    return np.array([[np.cos(m.radians(theta)),-np.sin(m.radians(theta))],[np.sin(m.radians(theta)),np.cos(m.radians(theta))]])

class PathShape(Enum):
    STATIC = 0
    LINE = 1
    CIRCLE = 2

class RotationType(Enum):
    CONTINUOUS = 0
    CONTINUOUS_BnF = 1

def createMeasurementSet(
                frames=1,
                shape=PathShape.STATIC,
                rotation=RotationType.CONTINUOUS,
                speed=0,
                rotSpeed=0,
                initialPos=[1,1],
                initialLidarAngle=0,
                counterclockwise=True,
                center=[0,0],
                direction=315):
    """ Base, general function for measurement sets """


    #Setup
    angle = initialLidarAngle
    points = []

    if not(shape is PathShape.STATIC) and speed==None:
        raise ValueError("Please assign a speed")

# Umbrella strategy: Converting to the center's coordinate system, doing
# efficiently the heavy calculation and going back to origin coordinate system

    #Base change
    position_cen = np.array(initialPos) - np.array(center)

    #Determine the new_position function
    if shape is PathShape.CIRCLE:
        try:
            angle = speed/(np.linalg.norm(position_cen))
        except ZeroDivisionError:
            print("The initial position and the center cannot be the same")
            raise
        transform = rotation(angle)
        new_position = transform.dot

    elif shape is PathShape.LINE:
        dirRotation = rotation(direction)
        transform = dirRotation.dot(speed)
        new_position = lambda pos: pos+transform
    else:
        #print("The LiDAR path shape defaults to static")
        new_position = lambda pos: pos

    #Create the data
    for f in range(frames):
        #New measurement
        points.append([[position_cen+np.array(center), angle]])

        #Increment
        position_cen = new_position(position_cen)
        angle += rotSpeed
        angle = angle%360

    return points


def measure_turn(pos, n=1, rSpeed=1):
    ''' The way the simulation behaves in current versions '''

    f = int((360*n)/rSpeed)
    return createMeasurementSet(frames=f, rotSpeed= rSpeed, initialPos=pos)

class Scheduler:
    def __init__(self, points, maxBatchSize=None):
        self.points = points
        self.index = 0
        self.maxIndex = len(points)-1
        self.complete = False

        self.maxBatchSize = maxBatchSize

    def getNextBatch(self):
        if (self.maxBatchSize == None):
            batchSize = len(points)
        else:
            batchSize = np.random.randInt(1, self.maxBatchSize+1)

        batch = []

        if (self.index+batchSize)>=self.maxIndex:
            # TODO: Raise exception if complete already true
            self.complete = True
            batchSize = self.maxIndex-self.index+1

        for k in range(batchSize):
            batch.append(self.points[k+self.index])

        self.index += batchSize

        return batch
