# Triangle Area Using Class 
# Comprehensive-06 (Chapter-04)

import math


class Triangle:
    def __init__(self, a, b, c):
        if a + b > c and b + c > a and c + a > b:
            s = (a + b + c) / 2
            Area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print("The area of the triangle is = ", Area)
        else:
            print("Triangle is not possible!")


a = int(input("Enter the first Arm = "))
b = int(input("Enter the second Arm = "))
c = int(input("Enter the third Arm = "))
triangle = Triangle(a, b, c)
