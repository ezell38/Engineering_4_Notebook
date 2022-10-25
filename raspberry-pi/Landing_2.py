import board
import math
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import time 
import digitalio  
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

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP21)      #Initializes OLED screen
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

def area_calc(x1, y1, x2, y2, x3, y3):
    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    area = abs((x1*y2+x2*y3+x3*y1-y1*x2-y2*x3-y3*x1)/2)
    return area

while True:

    try:
        [xcoor1, ycoor1] = input("Enter first coordinates in x,y format: ").split(",")
        [xcoor2, ycoor2] = input("Enter second coordinates in x,y format: ").split(",")
        [xcoor3, ycoor3] = input("Enter third coordinates in x,y format: ").split(",")
        area = area_calc(xcoor1,ycoor1,xcoor2,ycoor2,xcoor3,ycoor3)
        print(f"The area of the triangle with points ({xcoor1},{ycoor1}), ({xcoor2},{ycoor2}), and ({xcoor3},{ycoor3}) is {area} square km")


        splash = displayio.Group()


        triangle = Triangle(int(xcoor1) + 64, -int(ycoor1) + 32, int(xcoor2) + 64, -int(ycoor2) + 32, int(xcoor3) + 64, -int(ycoor3) + 32, outline=0xFFFF00)       #Print triangle on OLED screen, have to add 32 and 64 to put them in the right place on OLED screen
        splash.append(triangle)

        hline = Line(0,32,128,32, color=0xFFFF00)       #Print hon=rizontal line
        splash.append(hline)

        hline = Line(64,0,64,64, color=0xFFFF00)        #Print vertical line
        splash.append(hline)

        circle = Circle(64, 32, 2, outline=0xFFFF00)    #Prints center circle 
        splash.append(circle)

        display.show(splash)

    except:
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!")
        

   
   
 
   
