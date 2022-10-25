import board
import math

def area_calc(x1, y1, x2, y2, x3, y3):                      
    x1 = float(x1)                                              #Make entered coordinate a number the program can do math with
    x2 = float(x2)
    x3 = float(x3)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    area = abs((x1*y2+x2*y3+x3*y1-y1*x2-y2*x3-y3*x1)/2)         #Area of a triangle
    return area
while True: 

    try:
        [xcoor1, ycoor1] = input("Enter first coordinates in x,y format: ").split(",")  #The split function splits the two entered coordinates so they can then be floated and put into area formula
        [xcoor2, ycoor2] = input("Enter second coordinates in x,y format: ").split(",") #Sets entered coordinates as the official program coordinates
        [xcoor3, ycoor3] = input("Enter third coordinates in x,y format: ").split(",")
        area = area_calc(xcoor1,ycoor1,xcoor2,ycoor2,xcoor3,ycoor3)                        #Entered coordinates are used in the area function
        print(f"The area of the triangle with points ({xcoor1},{ycoor1}), ({xcoor2},{ycoor2}), and ({xcoor3},{ycoor3}) is {area} square km")

    except:
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!")       #If they don't enter in x,y syntax print this 
        