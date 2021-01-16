import keyboard
from keyboard import press
import mouse
from time import sleep
import json
import math

# https://www.thepythoncode.com/article/control-mouse-python

# it blocks until ctrl is pressed 
#keyboard.wait('Ctrl') 

# It writes the content to output 
#keyboard.write("hey guys look at this aint it cool") 

#sleep(2)

#keyboard.write("sanghoon")

#sleep(1)

#mouse.move(100, 100, absolute=False, duration=0.2)

#for i in range(5):
#    press("enter")

# left click

#mouse.click('left')

#keyboard.write("now im over here")




#JSON stuff:
#with open('vertices_19.json') as json_file:
#    data = json.load(json_file)
#    for p in data['topView']:
#        print(p[''])



with open('vertices_19.json') as file:
  data = json.load(file)

print(data["topView"])
topviewpoints = data["topView"]
print(topviewpoints[3][1]) 

## coordinates for a horizontal line (top of square)
#x1 = topviewpoints[0][0]
#x2 = topviewpoints[1][0]
#y1 = topviewpoints[0][1]
#y2 = topviewpoints[1][1]

## coordinates for a vertical line (right side of square)
#x1 = topviewpoints[1][0]
#x2 = topviewpoints[2][0]
#y1 = topviewpoints[1][1]
#y2 = topviewpoints[2][1]

## coordinates for slanted line
x1 = 50
x2 = 100
y1 = 50
y2 = 150

def riserun(x1, y1, x2, y2):
  if (x2 == x1): 
    return math.degrees(90)
  else:
    return (y2 - y1)/(x2 - x1)

print(round(math.degrees(math.atan( riserun(x1, y1, x2, y2))), 1))
