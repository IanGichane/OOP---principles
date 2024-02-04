# defining a class 
class ClassName:

    # define attributes and methods

    pass

import math 
class Circle:
    def __init__(self,radius):
        self.radius = radius#attribute

    def calculate_area(self):
        return round(math.pi * self.radius**2.2)

cir1 = Circle(14)
print(cir1.calculate_area())


#naming conventions
#public vs private
#WHY USE CLASSES
Model and solve real world problems
Reuse code 
Encapsulate data and behaviors in a single entity
