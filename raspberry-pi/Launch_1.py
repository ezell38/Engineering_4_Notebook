# Elias Zell
# Launch 1
# A countdown timer from 10-liftoff

import time 
import digitalio
import board 

led=digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT

for x in range(10, 0, -1): # This tells the function to count down from 10. The -1 means count down by one and the 0 means stop at 0. 
    print(x)                   #Count down in serial moniter
    time.sleep(1)

print("liftoff")
