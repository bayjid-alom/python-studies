class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name, "was adopted.")

    def run(self):
        print("Running!")


class Dog(Animal):
    def bark(self):
        print("Woof!")


# সরাসরি Animal ক্লাসের জন্য
# zuzu = Animal("zuzu")
# zuzu.run()


# Dog এর আউটপুটের জন্য, কিন্তু আউটপুটে Animal এর বৈশিষ্ট চলে আসছে।
spot = Dog("Spot")
spot.bark()

# Animal Class থেকে 
spot.run()


