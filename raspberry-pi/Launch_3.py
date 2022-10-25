# Elias Zell
# Launch 3
# A countdown timer from 10-liftoff

import time 
import digitalio
import board 

led1=digitalio.DigitalInOut(board.GP13)             #Set up both leds and button
led2=digitalio.DigitalInOut(board.GP18)
button=digitalio.DigitalInOut(board.GP17)


led1.direction=digitalio.Direction.OUTPUT
led2.direction=digitalio.Direction.OUTPUT
button.direction=digitalio.Direction.INPUT  
button.pull = digitalio.Pull.UP                 # Button is pulled up so when pressed will read as true
#print(button.value)

if button.value == True:                    #Once the button is pressed, initiate this function
    for x in range(10, 0, -1):
        print(x)
        led2.value=True
        time.sleep(.5)
        led2.value=False
        time.sleep(1)


    print("liftoff")
    led1.value=True
    time.sleep(5)

if button.value == False:                  #If the button hasn't been pressed, initiate this function
   print(button.value)