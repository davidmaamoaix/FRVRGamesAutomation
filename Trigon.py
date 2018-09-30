#Trigon

from pyautogui import screenshot,keyDown,keyUp,PAUSE

PAUSE=0

def run():
    while 1:
        screen=screenshot()
        color=convert(screen.getpixel((1280,1280)))
        c=nextColor(screen)
        if(c!=-1):
            if color>c:
                c+=3
            #print('{} {}'.format(c,color) )
            #color=screen.getpixel((1280,1280))
            for i in range(0,c-color):
                keyDown('Space')
                keyUp('Space')
                

def nextColor(screen):
    for i in range(725,675,-1):
        a=convert(screen.getpixel((1280,i)))
        if a!=-1:
            return a
    return -1

def convert(rgb):
    if rgb[0]>180 and rgb[1]>180 and 210>rgb[2]>180:
        return 0 #White
    if rgb[0]>rgb[1]+rgb[2]:
        return 1 #Red
    if rgb[1]>rgb[0] and rgb[1]>rgb[2] and rgb[1]>160:
        return 2 #Green
    return -1

run()
