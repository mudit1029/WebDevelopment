people = [
	{"Name": "Mudit" , "House": "Cheetah"},
	{"Name": "Anurag" , "House": "Saroj"},
	{"Name": "Adab" , "House": "Red"}
]

people.sort(key=lambda person : person["Name"])

print(people)