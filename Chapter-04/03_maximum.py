# Maxumum between three integer nummbers Using Class in python.
# Comprehensive-01 (Chapter-04)


class find_maximum:
    def __init__(self, a, b, c):
        if a > b and a > c:
            print(a, "is the largest number.")
        elif b > a and b > c:
            print(b, "is the largest number.")
        else:
            print(c, "is the largest number.")


a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))

maximum = find_maximum(a, b, c)
