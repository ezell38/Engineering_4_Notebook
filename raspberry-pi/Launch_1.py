# Elias Zell
# Launch 1
# A countdown timer from 10-liftoff

import time 
import digitalio
import board 

led=digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT

for x in range(10, 0, -1):
    print(x)
    time.sleep(1)

print("liftoff")
