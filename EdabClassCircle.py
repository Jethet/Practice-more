# Your task is to create a Circle constructor that creates a circle with a
# radius provided by an argument. The circles constructed must have two
# getters getArea() (PIr^2) and getPerimeter() (2PI*r) which give both
# respective areas and perimeter (circumference).
#For help with this class, I have provided you with a Rectangle constructor
# which you can use as a base example.

import math
# BOTH SOLUTIONS COPIED FROM EDABIT - I do not know enough math
class Circle:
    def __init__(self, radius):
  	self.radius = radius

    def getArea(self):
        return round(math.pi*(self.radius**2))

    def getPerimeter(self):
        return round(2*math.pi*self.radius)

class Circle:

	def __init__(self, radius = 0):
		self.radius = radius

	def getArea(self):
		return ((math.pi)*(self.radius**2))+1

	def getPerimeter(self):
		return (2 * (math.pi) * self.radius)+1


circy = Circle(11)
circy.getArea()

#Should return 380.132711084365.

circy = Circle(4.44)
circy.getPerimeter()

#Should return  27.897342763877365
