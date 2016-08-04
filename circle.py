class Circle(object):
	
	pi = 3.14159265358979323846264338327950
	
	def __init__ (self, radius):
		self.radius = radius
	
	def circumference(self):
		circumference = 2 * self.pi * self.radius
		return circumference
	
	def area(self):
		area = self.pi * (self.radius**2)
		return area
		
big_circle = Circle(10)
print(big_circle.circumference())
print(big_circle.area())