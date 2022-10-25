# Elias Zell
# Crash 2

import time 
import digitalio  
import board 
import adafruit_mpu6050
import busio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
led=digitalio.DigitalInOut(board.GP18)

mpu = adafruit_mpu6050.MPU6050(i2c) 

led.direction=digitalio.Direction.OUTPUT

mpu.acceleration 
mpu.gyro



while True: 

    print(f"X Acceleration: {mpu.acceleration[0]} m/s2")
    print(f"Y Acceleration: {mpu.acceleration[1]} m/s2")
    print(f"Z Acceleration: {mpu.acceleration[2]} m/s2")
    print("") 
    
    print("")
    time.sleep(.5)

    if mpu.acceleration[0]>9 or mpu.acceleration[1]>9 or mpu.acceleration[0]<-9 or mpu.acceleration[1]<-9:              #If the accelerometer is tilted more than 90 degrees run function
    
        led.value=True 

    else:                                                           #If not run this
        led.value=False    