from enum import Enum
import numpy as np

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
    """ Base function for measurement sets


    """


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
        print("The shape defaults to static")
        new_position = lambda pos: pos

    #Create the data
    for f in range(frames):
        #New measurement
        points.append([[position_cen, angle]])

        #Increment
        position_cen = new_position(position_cen)
        angle += rotSpeed

    #Reverting to
    return points

print(createMeasurementSet(frames=4, rotSpeed=1))
