# Elias Zell
# Launch 2
# A countdown timer from 10-liftoff

import time 
import digitalio
import board 

led1=digitalio.DigitalInOut(board.GP13)
led2=digitalio.DigitalInOut(board.GP18)
button=digitalio.DigitalInOut(board.GP17)


led1.direction=digitalio.Direction.OUTPUT
led2.direction=digitalio.Direction.OUTPUT
button.direction=digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
#print(button.value)

if button.value == True: 
    for x in range(10, 0, -1):
        print(x)
        led2.value=True
        time.sleep(.5)
        led2.value=False
        time.sleep(1)


    print("liftoff")
    led1.value=True
    time.sleep(5)

if button.value == False: 
   print(button.value)