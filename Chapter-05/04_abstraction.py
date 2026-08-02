"""
অ্যাবস্ট্রাকশন (Abstraction): অ্যাবস্ট্রাকশন হচ্ছে ক্লাসের অভ্যন্তরে ডাটা এবং ফাংশনকে ক্লাসের বাহির হতে অবাঞ্ছিত অ্যাক্সেস হতে সুরক্ষা প্রদান করে। নিচের প্রোগ্রামের Dog ক্লাসের মেম্বার নয় এরূপ, অবজেক্টের মাধ্যমে Dog ক্লাসের ফাংশনসমূহ অ্যাক্সেস দিবে না।
"""


class Dog:
    def __init__(self, name):
        self.name = name
        print(self.name, "was adopted")

    def bark(self):
        print("Woooof!")


spot = Dog("spot")
spot.bark()
