import sys

try:
	x = int(input("X: "))
	y = int(input("Y: "))

except ValueError:
	print("Error: Invalid Input")
	sys.exit(1)
if x > y:
	print("X is greater")

elif x == y:
	print("Both Are Equal")	

else:
	print("X is smaller")	