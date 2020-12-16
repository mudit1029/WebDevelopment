class Flight():
	def __init__(self , capacity):
		self.capacity = capacity
		self.passenger = []

	def add_passenger(self , name):
		if not self.open_seats():
			return False
		self.passenger.append(name)
		return True

	def open_seats(self):
		return self.capacity - len(self.passenger)

flight = Flight(3)

people = ["Mudit", "Anurag" , "Kuldeep" , "Adab"]

for person in people:
	success = flight.add_passenger(person)	
	if success:
		print(f"{person} added to flight Successfully")
	else:
		print(f"No Seats For {person} ")		

			