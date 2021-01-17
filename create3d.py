import keyboard
from keyboard import press
import mouse
from time import sleep
import json
import math
import calculations

# https://www.thepythoncode.com/article/control-mouse-python


# Load in JSON data
with open('pointdata.json') as file:
    data = json.load(file)

# Store top, front, and side view coordinates as 2D arrays
sideviewpoints = data["sideView"]
topviewpoints = data["topView"]
frontviewpoints = data["frontView"]

# creates 2d array of lengths and angles
lenAngleData = []

for i in range(1, len(topviewpoints)):
  x1 = topviewpoints[i-1][0]
  x2 = topviewpoints[i][0]
  y1 = topviewpoints[i-1][1]
  y2 = topviewpoints[i][1]

  lenAngleData.append( [calculations.lenCalc(x1, y1, x2, y2), 
                        calculations.degCalc(x1, y1, x2, y2)] )


# prep arrays

# get width length height and make first instructions from that

# get cuts from each surface and make instructions from that
