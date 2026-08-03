"""
Abstraction : এবস্ট্রাকশন হচ্ছে ক্লাসের অভ্যন্তরে ডাটা এবং ফাংশনকে ক্লাসের বাহির হতে অবাঞ্চিচ এক্সেস হতে সুরক্ষা প্রদান করা।
"""

# Short-Question-06 (Chapter-04)


class Dog:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} was adopted.")

    def bark(self):
        print("Woof!")

    def calling(self):
        print(f"Hey {self.name} come here.")


object1 = Dog("Zuzu")
object1.bark()
object1.calling()
