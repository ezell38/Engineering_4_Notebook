# Elias Zell
# Launch 2
# A countdown timer from 10-liftoff

import time 
import digitalio
import board 

led1=digitalio.DigitalInOut(board.GP13)         #Set led1 and led2 to control both leds and make them do seperate things.
led2=digitalio.DigitalInOut(board.GP18)
button=digitalio.DigitalInOut(board.GP17)


led1.direction=digitalio.Direction.OUTPUT       #Green led
led2.direction=digitalio.Direction.OUTPUT       #Red led


for x in range(10, 0, -1):
    print(x) 
    led2.value=True             
    time.sleep(.5)
    led2.value=False
    time.sleep(1)


    print("liftoff")
    led1.value=True
    time.sleep(5)

