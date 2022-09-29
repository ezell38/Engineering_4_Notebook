def add_numbers(x, y):
	total = float(x) + float(y)
	return total

while True:

    x = input("First Number:")
    y = input("Second Number:")

    try:
        sum = add_numbers(x,y)
        print(f"The sum of {x} and {y} is {sum}")

    except:
        print("Only integers are allowed, try again")

