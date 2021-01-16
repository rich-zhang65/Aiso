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

# returns the main four corners of a sketch (rectangular base)
def getFourCorners(pointsArray):

  topRight = pointsArray[0]
  topLeft = pointsArray[0]
  bottomRight = pointsArray[0]
  bottomLeft = pointsArray[0]

  for i in range(len(pointsArray)):

    if pointsArray[i][0] < topLeft[0] or pointsArray[i][1] < topLeft[1]:
      topLeft = pointsArray[i]
    
    if pointsArray[i][0] > topRight[0] or pointsArray[i][1] < topRight[1]:
      topRight = pointsArray[i]

    if pointsArray[i][0] > bottomRight[0] or pointsArray[i][1] > bottomRight[1]:
      bottomRight = pointsArray[i]

    if pointsArray[i][0] < bottomLeft[0] or pointsArray[i][1] > bottomLeft[1]:
      bottomLeft = pointsArray[i]
  
  # sketchy fix (repeat for other cases once example 1 works)
  #basically wanna make sure it makes a rectangle shape for now
  if topLeft[1] != topRight[1]:
    if topLeft[1] > topRight[1]:
      topRight[1] = topLeft[1]

  if topRight[0] != bottomRight[0]:
    if topRight[0] < bottomRight[0]:
      topRight[0] = bottomRight[0]

  return [topLeft, topRight, bottomRight, bottomLeft]


# given a surface sketch, it finds the coordinates of the shapes we need to cut out
# only one cut for now
# works with "chronological" drawing
def getCuttingShapes(pointsArray):
    
  corners = getFourCorners(pointsArray)

  cutPoints = []

  for i in range(len(pointsArray)):

      # find cuts that are not part of the corners
    if pointsArray[i] not in corners:
      cutPoints.append(pointsArray[i])    

  for i in range(len(corners)):

    if corners[i] not in pointsArray:
      cutPoints.append(corners[i])

  return cutPoints
