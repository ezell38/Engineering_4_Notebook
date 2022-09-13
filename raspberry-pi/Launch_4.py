# Elias Zell
# Launch 4
# A countdown timer from 10-liftoff

import time 
import digitalio
import board 
import pwmio
from adafruit_motor import servo


led1=digitalio.DigitalInOut(board.GP13)
led2=digitalio.DigitalInOut(board.GP18)
button=digitalio.DigitalInOut(board.GP17)

pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)



led1.direction=digitalio.Direction.OUTPUT
led2.direction=digitalio.Direction.OUTPUT
button.direction=digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN
#print(button.value)

while True:

    if button.value == True: 
        for x in range(10, 0, -1):
            print(x)
            led2.value=True
            time.sleep(.5)
            led2.value=False
            time.sleep(1)


        print("liftoff")
        led1.value=True
        servo1.angle = 0
        time.sleep(5)



        