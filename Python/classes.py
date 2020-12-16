class point():
	def __init__(self, x ,y):
		self.x = x
		self.y = y
X = int(input("X:"))
Y = int(input("Y:")) 
p = point({X} , {Y})

print(f"X Co-ordinate = {p.x} and Y Co-ordinate = {p.y}")		