# Elias Zell
# Launch 2
# A countdown timer from 10-liftoff

import time 
import digitalio
import board 

led1=digitalio.DigitalInOut(board.GP13)
led2=digitalio.DigitalInOut(board.GP18)

led1.direction=digitalio.Direction.OUTPUT
led2.direction=digitalio.Direction.OUTPUT

for x in range(10, 0, -1):
    print(x)
    led1.value=True
    time.sleep(.5)
    led1.value=False
    time.sleep(1)

print("liftoff")
led2.value=True
time.sleep(.5)
led2.value=False