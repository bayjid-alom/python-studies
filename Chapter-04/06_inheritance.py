class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name, "is adopted")

    def run(self):
        print("Running!")


class Dog(Animal):
    def bark(self):
        print("Wooooof!")


spot = Dog("Zuzu")
spot.bark()
