#Dart

from time import sleep
from pyautogui import moveTo,mouseDown,mouseUp

def throw(center=True):
    moveTo(640,600)
    mouseDown()
    moveTo(640,300 if center else 265)
    mouseUp()

while 1:
    for i in [0,0,0,0,1]:
        throw(i)
        sleep(2)
    
