import keyboard
from keyboard import press
import mouse
from time import sleep

# https://www.thepythoncode.com/article/control-mouse-python

# it blocks until ctrl is pressed 
keyboard.wait('Ctrl') 

# It writes the content to output 
keyboard.write("hey guys look at this aint it cool") 

sleep(2)

keyboard.write("sanghoon")

sleep(1)

mouse.move(100, 100, absolute=False, duration=0.2)

for i in range(5):
    press("enter")

# left click
mouse.click('left')

keyboard.write("now im over here")
