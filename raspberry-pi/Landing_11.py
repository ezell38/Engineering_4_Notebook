def area_calc(x, y):
	area = float(x) + float(y)
	return total

while True:

    Cor1 = input("Enter the first coordinate in x,y format:")
    Cor2 = input("Enter the second coordinate in x,y format:")
    Cor3 = input("Enter the third coordinate in x,y format:")
  

    try:
        area = area_calc(Cor1,Cor2,Cor3)
        print(f"The area of the triangle with verticies {Cor1}, {Cor2}, and {Cor3} is {Area} square km")

    except:
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!")
