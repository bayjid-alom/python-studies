class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name, "was adopted.")

    def run(self):
        print("Running!")


class Tortoise(Animal):
    def run(self):
        print("Running slowly!")


# animal = Animal("zuzu")
# animal.run()

"""সেকেন্ড ক্লাসের জন্য আরগুমেন্ট পাস করলেও সেটা Animal ক্লাসের জন্য আউটপুট দিচ্ছে। """
tim = Tortoise("Tim")
tim.run()





