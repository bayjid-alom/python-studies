# Program-5 TB-Page:86

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        Area = math.pi * (self.radius**2)
        print("Circle Area is = ", Area)


radius = int(input("Enter circle radius = "))
circle = Circle(radius)
circle.circle_area()
