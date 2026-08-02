"""
ইনহেরিট্যান্স (Inheritance) : ইনহেরিট্যান্স হচ্ছে এক ধরনের মেকানিজম, যেখানে চাইল্ড ক্লাস তৈরির সময় পেরেন্ট ক্লাসের বিহেভিয়ার ও প্রোপার্টিজ ধারণ করে। নিচের প্রোগ্রামে Animal হচ্ছে পেরেন্ট ক্লাস, Dog হচ্ছে চাইল্ড ক্লাস, Dog ক্লাস Animal ক্লাসের বৈশিষ্ট্য ধারণ করছে। spot হচ্ছে Dog ক্লাসের মেম্বার কিন্তু এর মাধ্যমে Animal ক্লাসের মেম্বারসমূহকে অ্যাক্সেস করা যাচ্ছে, এটাকে ইনহেরিট্যান্স বলে।
"""


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
