import keyboard
from keyboard import press
import mouse
from time import sleep
import json
import math
import calculations
import flask

# mouse keyboard stuff
# https://www.thepythoncode.com/article/control-mouse-python


# app = Flask(__name__)

# @app.route('/')
# def index():
#   return render_template('aisoDrawingPad.html')




# Load in JSON data
with open('vertices_19.json') as file:
  data = json.load(file)

# Store top, front, and side view coordinates as 2D arrays
topviewpoints = data["topView"]
frontviewpoints = data["frontView"]
sideviewpoints = data["sideView"]

# to create a closed shape, must "connect" first item 
#  of array to last item of array
# topviewpoints.append(topviewpoints[0])
# frontviewpoints.append(frontviewpoints[0])
# sideviewpoints.append(sideviewpoints[0])

def riserun(x1, y1, x2, y2):
  if (x2 == x1): 
    return math.degrees(90)
  else:
    return (y2 - y1)/(x2 - x1)

def degCalc(x1, y1, x2, y2):
  return round(math.degrees(math.atan( riserun(x1, y1, x2, y2))), 1)

def lenCalc(x1, y1, x2, y2):
  return 1
  #return round(math.sqrt( (x2 - x1)^2 + (y2 - y1)^2 ), 1)

## creates 2d array of lengths and angles
lenAngleData = []

for i in range(1, len(topviewpoints)):
  x1 = topviewpoints[i-1][0]
  x2 = topviewpoints[i][0]
  y1 = topviewpoints[i-1][1]
  y2 = topviewpoints[i][1]

  lenAngleData.append( [lenCalc(x1, y1, x2, y2), 
                        degCalc(x1, y1, x2, y2)] )

# print(lenAngleData)
# print(calculations.overallLength(topviewpoints))

newpoints = calculations.prepArray(sideviewpoints)

print(newpoints)

print(calculations.getFourCorners(newpoints))

print(newpoints)

print(calculations.getCuttingShape(newpoints))

# lenAngleArrayMaker usage for top, front, and side
#print(calculations.lenAngleArrayMaker(topviewpoints))
#print(calculations.lenAngleArrayMaker(frontviewpoints))
#print(calculations.lenAngleArrayMaker(sideviewpoints))
