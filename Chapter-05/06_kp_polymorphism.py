class Bird:
    def sound(self):
        print("Bird makes sound")


class Cat:
    def sound(self):
        print("Cat says meow")


class Dog:
    def sound(self):
        print("Dog says woof")


for animal in [Bird(), Cat(), Dog()]:
    animal.sound()
