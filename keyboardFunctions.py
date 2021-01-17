import keyboard
from keyboard import press
import mouse
from time import sleep
import math

#commands for drawing rectangle
def drawRectangle(length, width):

    mouse.click('left')
    mouse.move(0, width*-1, absolute=False, duration=0.5) #first two inputs: right, down

    mouse.click('left')
    mouse.move(length, 0, absolute=False, duration=0.5)

    mouse.click('left')
    mouse.move(0, width, absolute=False, duration=0.5)

    mouse.click('left')
    mouse.move(length*-1, 0, absolute=False, duration=0.5)

    mouse.click('left')

def extrude(height):

    #mouse.move(50, -50, absolute=False, duration=1)

    #mouse.click('left')

    mouse.move(365, -55, absolute=False, duration=0.5)
    
    sleep(0.3)

    mouse.click('left')

    keyboard.write(str(height))

    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')

def extrudeCut(depth):

    keyboard.press_and_release('s')

    mouse.move(25, 100, absolute=False, duration=0.5)

    sleep(0.3)

    mouse.click('left')

    keyboard.write(str(depth))

    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')