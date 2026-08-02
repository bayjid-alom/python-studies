"""
এনক্যাপসুলেশন (Encapsulation): ক্লাসের মেম্বারসমূহ (ভেরিয়েবল, মেথড এবং অবস্থা) অ্যাক্সেস করার পদ্ধতিকে এনক্যাপসুলেশন বলে। ক্লাসের মেম্বারসমূহ পাবলিক হিসাবে থাকে, যদি প্রাইভেট হিসাবে ঘোষণা না করা হয়।
+ অবাঞ্চিত এক্সেস রোধ করে।

Syntax	            অর্থ
self.password	    Public (সবার জন্য উন্মুক্ত)
self._password	    Protected (Convention অনুযায়ী internal)
self.__password	    Private (Name mangling-এর মাধ্যমে সরাসরি access কঠিন করা হয়)
"""


class Student:
    def __init__(self, name, password):
        self.name = name
        self.__password = password


student1 = Student("Bayjid", "12345")

print(student1.name)  # ✅ Accessible
# print(student1.__password)  # ❌ Error (Private)
