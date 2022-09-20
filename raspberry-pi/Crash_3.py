# Elias Zell
# Crash 1

import time 
import digitalio  
import board 
import adafruit_mpu6050
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays() #put this line just below your imports


sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
led=digitalio.DigitalInOut(board.GP18)

display_bus = displayio.I2CDisplay(i2c, device_address=['0x3d', '0x68'], reset=board.GP21)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

mpu = mpu = adafruit_mpu6050.MPU6050(i2c, address=['0x3d', '0x68'])

led.direction=digitalio.Direction.OUTPUT



mpu.acceleration 
mpu.gyro

splash = displayio.Group()

# add title block to display group
title = "ANGULAR VELOCITY"
# the order of this command is (font, text, text color, and location)
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    

# you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
# Don't forget to round the angular velocity values to three decimal places

# send display group to screen
display.show(splash)




while True: 

    print(f"X Acceleration: {mpu.acceleration[0]} m/s2")
    print(f"Y Acceleration: {mpu.acceleration[1]} m/s2")
    print(f"Z Acceleration: {mpu.acceleration[2]} m/s2")
    print("") 
    
    print("")
    time.sleep(.2)

    if mpu.acceleration[0]>9 or mpu.acceleration[1]>9 or mpu.acceleration[0]<-9 or mpu.acceleration[1]<-9:
    
        led.value=True 

    else:
        led.value=False  
   
   
 
   
 