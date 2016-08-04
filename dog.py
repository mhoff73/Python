class Dog(object):
	
	species = "mammal"
	
	def __init__(self, breed, size, color, name):
		self.breed = breed
		self.size = size
		self.color = color
		self.name = name
		
	def bark(self):
		if self.size < 20:
			print("woof!")
		else:
			print("WOOF!!")
		
ellie = Dog("Lab", 60, "golden", "ellie")
nala = Dog("Yorkie", 10, "brown", "nala")
print(ellie.breed)
print(nala.breed)
ellie.bark()
nala.bark()