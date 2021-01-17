import keyboard
from keyboard import press
import mouse
from time import sleep
import math

#commands for drawing rectangle
def drawRectangle(length, width):

    mouse.click('left')
    mouse.move(0, width*-1, absolute=False, duration=1) #first two inputs: right, down

    mouse.click('left')
    mouse.move(length, 0, absolute=False, duration=1)

    mouse.click('left')
    mouse.move(0, width, absolute=False, duration=1)

    mouse.click('left')
    mouse.move(length*-1, 0, absolute=False, duration=1)

    mouse.click('left')