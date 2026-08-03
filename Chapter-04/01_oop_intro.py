"""
✔️ OOP(Object-Oriented Programming) -এর ৪টি Pillars:

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism"""


class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def introduce(self):

        print(f"My name is {self.name}. My Roll no is {self.roll}")


student1 = student("Jihad", 241118)
student1.introduce()
