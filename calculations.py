# a library with all of our calculations to be imported into create3d.py
import math

def lenAngleArrayMaker(pointsArray):
  dataArray = []
  pointsArray.append(pointsArray[0])

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
    return farRight[0] - farLeft[0]


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
    return farUp[1] - farDown[1]


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
  return farUp[1] - farDown[1]

# returns the main four corners of a sketch (rectangular base)
def getFourCorners(pointsArray):

  copyPointsArray = pointsArray[:]

  maxes = findMaxes(copyPointsArray)
  mins = findMins(copyPointsArray)
  print(maxes, mins)
  
  # sketchy fix (repeat for other cases once example 1 works)
  #basically wanna make sure it makes a rectangle shape for now
  # if topLeft[1] != topRight[1]:
  #   if topLeft[1] > topRight[1]:
  #     topRight[1] = topLeft[1]

  #if topRight[0] != bottomRight[0]:
  #  if topRight[0] < bottomRight[0]:
  #    topRight[0] = bottomRight[0]
  return [[mins[0], mins[1]], [maxes[0], mins[1]], [mins[0], maxes[1]], [maxes[0], maxes[1]]]


# given a surface sketch, it finds the coordinates of the shapes we need to cut out
# only one cut for now
# works with "chronological" drawing
def getCuttingShape(pointsArray):
  
  copyPointsArray = pointsArray[:]

  corners = getFourCorners(copyPointsArray)
  cutPoints = []

  for i in range(len(copyPointsArray)):

    # find points that are not part of the corners
    if copyPointsArray[i] not in corners:
      cutPoints.append(copyPointsArray[i])    

  # find corners we need to include in cut
  for i in range(len(corners)):

    if corners[i] not in copyPointsArray:
      cutPoints.append(corners[i])

  return cutPoints

# removes uneccessary points from arrays
def prepArray(pointsArray):

  copyPointsArray = pointsArray[:]

  newArray = []

  firstPoint = copyPointsArray[0]

  for i in range(1,len(copyPointsArray)):

    if(copyPointsArray[i] == firstPoint):

      newArray = copyPointsArray[:i]
      return newArray
  
  return copyPointsArray

def findMaxes(pointsArray):

  maxX = pointsArray[0][0]
  maxY = pointsArray[0][1]

  for i in range(len(pointsArray)):
      
    if(pointsArray[i][0] > maxX):
      maxX = pointsArray[i][0]

    if(pointsArray[i][1] > maxY):
      maxY = pointsArray[i][1]

  return [maxX, maxY]

def findMins(pointsArray):

  minX = pointsArray[0][0]
  minY = pointsArray[0][1]

  for i in range(len(pointsArray)):
      
    if(pointsArray[i][0] < minX):
      minX = pointsArray[i][0]

    if(pointsArray[i][1] < minY):
      minY = pointsArray[i][1]

  return [minX, minY]

