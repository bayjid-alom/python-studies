class Rhombus:
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2


rhombus = Rhombus(10, 8)
print("Area of Rhombus:", rhombus.area())


"""
Output:
Area of Rhombus: 40.0
"""
