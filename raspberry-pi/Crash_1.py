# Elias Zell
# Crash 1

import time 
import digitalio  
import board 
import adafruit_mpu6050
import busio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

mpu = adafruit_mpu6050.MPU6050(i2c) 

mpu.acceleration 
mpu.gyro

while True: 
    
    print(f"X Acceleration: {mpu.acceleration[0]} m/s2")        #Print the X coordinate of the accelerometer
    print(f"Y Acceleration: {mpu.acceleration[1]} m/s2")        #Print the Y coordinate of the accelerometer
    print(f"Z Acceleration: {mpu.acceleration[2]} m/s2")        #Print the Z coordinate of the accelerometer
    print("") 
    
    print("")                                                   #Prints everything you just wrote above 
    time.sleep(1) 