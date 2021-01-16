import keyboard
from keyboard import press
import mouse
from time import sleep
import json
import math
import calculations
from flask import Flask, render_template

# mouse keyboard stuff
# https://www.thepythoncode.com/article/control-mouse-python


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('aisoDrawingPad.html')




# Load in JSON data
with open('vertices_19.json') as file:
  data = json.load(file)

# Store top, front, and side view coordinates as 2D arrays
topviewpoints = data["topView"]
frontviewpoints = data["frontView"]
sideviewpoints = data["sideView"]

# to create a closed shape, must "connect" first item 
#  of array to last item of array
topviewpoints.append(topviewpoints[0])
frontviewpoints.append(frontviewpoints[0])
sideviewpoints.append(sideviewpoints[0])



# lenAngleArrayMaker usage for top, front, and side
#print(calculations.lenAngleArrayMaker(topviewpoints))
#print(calculations.lenAngleArrayMaker(frontviewpoints))
#print(calculations.lenAngleArrayMaker(sideviewpoints))
