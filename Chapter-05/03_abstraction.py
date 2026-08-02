class Dog:
    def __init__(self, name):
        self.name = name
        print(self.name , "was adopted")

    def bark(self):
        print("Woooof!")

spot = Dog('spot')
spot.bark()
