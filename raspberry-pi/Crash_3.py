# Elias Zell
# Crash 3 

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

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP21)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

mpu = mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

led.direction=digitalio.Direction.OUTPUT



mpu.acceleration 
mpu.gyro


while True: 

    print(f"X Acceleration: {mpu.acceleration[0]} m/s2")
    print(f"Y Acceleration: {mpu.acceleration[1]} m/s2")
    print(f"Z Acceleration: {mpu.acceleration[2]} m/s2")
    print("") 
    
    print("")
    time.sleep(.2)

    splash = displayio.Group()                      #Print displayio.Group() on the OLED screen

    title = "ANGULAR VELOCITY"                                                              #What to print

    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)          #Where on the screen to print 
    splash.append(text_area)                                                                


    list = (f"X : {round(mpu.acceleration[0],3)} rad/s")                                    #This rounds the coordinate                           
                
    text_area = label.Label(terminalio.FONT, text=list, color=0xFFFF00, x=5, y=20) 
    splash.append(text_area)   


    money = (f"Y : {round(mpu.acceleration[1],3)} rad/s")
                
    text_area = label.Label(terminalio.FONT, text=money, color=0xFFFF00, x=5, y=30) 
    splash.append(text_area)   


    elias = (f"Z : {round(mpu.acceleration[2],3)} rad/s")
            
    text_area = label.Label(terminalio.FONT, text=elias, color=0xFFFF00, x=5, y=40) 
    splash.append(text_area)   


    display.show(splash)                                                                    #Print splash on the screen

        
    if mpu.acceleration[0]>9 or mpu.acceleration[1]>9 or mpu.acceleration[0]<-9 or mpu.acceleration[1]<-9:
    
        led.value=True 

    else:
        led.value=False  
   
   
 
   
