import keyboard
from keyboard import press
import mouse
from time import sleep
import json
import math
from calculations import * 
from keyboardFunctions import *

# https://www.thepythoncode.com/article/control-mouse-python


# Load in JSON data
with open('derulo.json') as file:
    data = json.load(file)

# Store top, front, and side view coordinates as 2D arrays
sideviewpoints = data["sideView"]
topviewpoints = data["topView"]
frontviewpoints = data["frontView"]

# creates 2d array of lengths and angles
# lenAngleData = []

# for i in range(1, len(topviewpoints)):
#   x1 = topviewpoints[i-1][0]
#   x2 = topviewpoints[i][0]
#   y1 = topviewpoints[i-1][1]
#   y2 = topviewpoints[i][1]

#   lenAngleData.append( [calculations.lenCalc(x1, y1, x2, y2), 
#                         calculations.degCalc(x1, y1, x2, y2)] )


# prep arrays (removes uneccessary points like lines inside the shape that aren't cuts)

sidePointsPrepped = prepArray(sideviewpoints)
topPointsPrepped = prepArray(topviewpoints)
frontPointsPrepped = prepArray(frontviewpoints)

# get width length height and make first instructions from that

baseLength = overallLength(topPointsPrepped)
baseWidth = overallWidth(topPointsPrepped)
baseHeight = overallHeight(sidePointsPrepped)

# get cuts from each surface and make instructions from that

sideSurfaceCuts = getCuttingShape(sidePointsPrepped)
topSurfaceCuts = getCuttingShape(topPointsPrepped)
frontSurfaceCuts = getCuttingShape(frontPointsPrepped)

print(baseLength)
print(baseWidth)
print(baseHeight)

print(sideSurfaceCuts)
print(topSurfaceCuts)
print(frontSurfaceCuts)

# keyboard commands ------------------------------------------------------------------------------------------------------------------

keyboard.wait('f')

keyboard.press('l')

keyboard.wait('f')

# sketch rectangle using lines
#drawRectangle(baseLength,baseWidth)

#extrude it so we now have our basic prism
# we haven't scaled height and pixels yet
#extrude(baseHeight/4)

#keyboard.wait('f')

drawRectangle(200,200)

extrudeCut(100)