# a library with all of our calculations to be imported into create3d.py
import math

def lenAngleArrayMaker(pointsArray):
  dataArray = []

  for i in range(1, len(pointsArray)):
    x1 = pointsArray[i-1][0]
    x2 = pointsArray[i][0]
    y1 = pointsArray[i-1][1]
    y2 = pointsArray[i][1]

    dataArray.append( [lenCalc(x1, y1, x2, y2), 
                       degCalc(x1, y1, x2, y2)] )

  return dataArray

def riserun(x1, y1, x2, y2):
  if (x2 == x1): 
    return math.degrees(90)
  else:
    return (y2 - y1)/(x2 - x1)

def degCalc(x1, y1, x2, y2):
  return round(math.degrees(math.atan( riserun(x1, y1, x2, y2))), 1)

def lenCalc(x1, y1, x2, y2):
  return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

# give this function the top view points to get the overall length
def overallLength(topViewPoints):
    
    # set variables for 4 extreme points
    farLeft = topViewPoints[0]
    farRight = topViewPoints[0]

    #loop through all the points, update extreme points
    for i in range(len(topViewPoints)):

      if topViewPoints[i][0] < farLeft[0]:
        farLeft = topViewPoints[i]

      if(topViewPoints[i][0] > farRight[0]):
        farRight = topViewPoints[i]

    #use len calc to get the length and return
    return lenCalc(farLeft[0], farLeft[1], farRight[0], farRight[1])


# give this function the top view points to get the overall width
def overallWidth(topViewPoints):

    # set variables for 4 extreme points
    farUp = topViewPoints[0]
    farDown = topViewPoints[0]

    #loop through all the points, update extreme points
    for i in range(len(topViewPoints)):

      if topViewPoints[i][1] > farUp[1]:
        farUp = topViewPoints[i]

      if(topViewPoints[i][1] < farDown[1]):
        farDown = topViewPoints[i]

    #use len calc to get the width and return
    return lenCalc(farUp[0], farUp[1], farDown[0], farDown[1])


# give this function the front or side view points to get the overall height
def overallHeight(sideViewPoints):
  
  # set variables for 4 extreme points
  farUp = sideViewPoints[0]
  farDown = sideViewPoints[0]

  #loop through all the points, update extreme points
  for i in range(len(sideViewPoints)):

    if sideViewPoints[i][1] > farUp[1]:
      farUp = sideViewPoints[i]

    if(sideViewPoints[i][1] < farDown[1]):
      farDown = sideViewPoints[i]

  #use len calc to get the height and return
  return lenCalc(farUp[0], farUp[1], farDown[0], farDown[1])


def getCuttingSurface(pointsArray):
    return 0