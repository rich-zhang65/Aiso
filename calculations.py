# a library with all of our calculations to be imported into create3d.py
import math

def riserun(x1, y1, x2, y2):
  if (x2 == x1): 
    return math.degrees(90)
  else:
    return (y2 - y1)/(x2 - x1)

def degCalc(x1, y1, x2, y2):
  return round(math.degrees(math.atan( riserun(x1, y1, x2, y2))), 1)

def lenCalc(x1, y1, x2, y2):
  return math.sqrt( (x2 - x1)^2 + (y2 - y1)^2 )

def overallLength(topViewPoints):
    return -1

def overallWidth(topViewPoints):
    return -1

def overallHeight(sideViewPoints):
    return -1

def getCuttingSurface(pointsArray):
    return 0