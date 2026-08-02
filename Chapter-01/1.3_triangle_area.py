import math


def triangle_area():
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    c = int(input("Enter the value of c : "))
    if a + b > c and b + c > a and c + a > b:
        s = (a + b + c) / 2
        Area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Triangle area is = ", Area)

    else:
        print("Triangle is not possible!")


triangle_area()
