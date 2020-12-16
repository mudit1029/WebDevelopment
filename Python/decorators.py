def announce(f):
	def wrapper():
		print("About To Run The Function")
		f()
		print("Done With The Function")
	return wrapper

@announce	
def hello():
	print("Hello, World!!")
		
hello()