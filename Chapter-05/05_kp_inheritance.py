# parent class


class Animal:
    def eat(self):
        print("Animal is eating")


# child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


# object make
d = Dog()

d.eat()  # from parent class
d.bark()  # from child class
