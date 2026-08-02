# Object-Oriented Programming (OOP)
> **Chapter Name: FOUR PILLARS OF OOP**

---

```
📝OOP-এর ৪টি Pillars In short - PIEA:

P - Polymorphism
I - Inheritance
E - Encapsulation
A - Abstraction
```
---
<br><br>








<!--🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 -->
<details>
<summary><strong>📝 উদাহরণসহ Encapsulation পদ্ধতি বর্ণনা কর। (রচনামূলক-৪)</strong></summary>

### উত্তর :
ক্লাসের মেম্বারসমূহ (ভেরিয়েবল, মেথড এবং অবস্থা) অ্যাক্সেস করার পদ্ধতিকে এনক্যাপসুলেশন বলে। ক্লাসের মেম্বারসমূহ পাবলিক হিসাবে থাকে, যদি প্রাইভেট হিসাবে ঘোষণা না করা হয়। 
নিচে একটি প্রোগ্রামের মাধ্যমে এনক্যাপসুলেশন পদ্ধতি দেখানো হলো-

### উদাহরণ

```python
class Person:
    def __init__(self, name, password):
        self.name = name            # Public Attribute
        self.__password = password  # Private Attribute

    def show_password(self):
        return self.__password


class Student(Person):
    def introduce(self):
        print(f"My name is {self.name}")


student1 = Student("Bayjid", "12345")

student1.introduce()
print(student1.show_password())

# print(student1.__password)   # ❌ Error
```

### Output

```text
My name is Bayjid
12345
```
---


### ব্যাখ্যা

উপরের প্রোগ্রামে `Person` ক্লাসে `name` একটি **Public Attribute**, তাই এটি ক্লাসের বাইরে থেকেও সহজেই ব্যবহার করা যায়। অন্যদিকে, `__password` একটি **Private Attribute**, ফলে এটি বাইরে থেকে সরাসরি Access করা সম্ভব নয়। Private Data নিরাপদভাবে ব্যবহারের জন্য `show_password()` নামে একটি **Public Method** ব্যবহার করা হয়েছে, যা `__password`-এর মান Return করে। এছাড়া `Student` ক্লাস, `Person` ক্লাসকে Inherit করায় এটি `Person`-এর সকল **Public Member** ব্যবহার করতে পারে। এভাবেই **Encapsulation** গুরুত্বপূর্ণ Data-কে সুরক্ষিত রেখে **Controlled Access** নিশ্চিত করে।

---

### সংক্ষিপ্ত নোট (Process)

- `__password` একটি **Private Attribute**, তাই Class-এর বাইরে থেকে সরাসরি Access করা যায় না।
- `show_password()` হলো একটি **Public Method**, যা Private Data নিরাপদভাবে Return করে।
- এভাবেই **Encapsulation** Data-কে সুরক্ষিত রাখে এবং **Controlled Access** প্রদান করে।

</details>
<br>












<!--🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 -->
<details>
<summary><strong>📝 প্রোগ্রামসহ পলিমরফিজম পদ্ধতি বর্ণনা কর। (রচনামূলক-০১)</strong></summary>

### উত্তর:

পলিমরফিজম (Polymorphism): পলি শব্দের অর্থ বহু, মরফিজম শব্দের অর্থ রূপ। পলিমরফিজম হচ্ছে বহুরূপ, যা এমন এক ধরনের বৈশিষ্ট্য, যেখানে একটি ফাংশন বা অবজেক্ট ভিন্ন ভিন্ন রূপে মূলত ফাংশনের আর্চমেন্ট বা ফাংশন কলের উপর নির্ভর করে ফলাফল প্রদান করে। নিচের প্রোগ্রামে উদাহরণ দেওয়া হলো-
---

### প্রোগ্রাম

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name, "was adopted.")

    def run(self):
        print("Running!")


class Turtle(Animal):
    def run(self):
        print("Running slowly!")


tim = Turtle("Tim")
tim.run()
```

### Output

```text
Tim was adopted.
Running slowly!
```
---
উপরের প্রোগ্রামে Turtle এবং Animal দুইটি ক্লাসের মধ্যে' run() নামক মেথড ডিফাইন করা হয়েছে। কলের উপর নির্ভর করে কোন মেথড রান হবে তা নির্ধারণ করে একই নামের একাধিক মেথড ভিন্ন ভিন্ন কাজ করাকে পলিমরফিজম বলে। Turtle ক্লাস Animal ক্লাসকে ইনহেরিট করবে। এখানে Animal ক্লাস হচ্ছে সুপার ক্লাস, Turtle ক্লাস সাব ক্লাস। Turtle ক্লাসে run() মেথড পুনরায় ডিফাইন করাকে মেথড ওভার-রাইডিং বলে।
---

### Method Overriding

`Turtle` Class-এ `run()` Method পুনরায় লিখে `Animal` Class-এর `run()` Method-এর নতুন আচরণ নির্ধারণ করা হয়েছে। একে **Method Overriding** বলা হয়।

---

### পলিমরফিজম-এর প্রকারভেদ

#### ১। Static / Compile-time Polymorphism
- Method Overloading
- Operator Overloading

#### ২। Dynamic / Run-time Polymorphism
- Method Overriding

---



### সংক্ষিপ্ত নোট (Process / Not write in exam)

- **Polymorphism** অর্থ **একই Method-এর একাধিক রূপ**।
- এটি সাধারণত **Method Overriding** বা **Method Overloading**-এর মাধ্যমে বাস্তবায়ন করা হয়।
- Python-এ সবচেয়ে বেশি ব্যবহৃত হয় **Run-time Polymorphism (Method Overriding)**।

</details>
<br>












<!--🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 -->
<details>
<summary><strong>📝 উদাহরণসহ ইনহেরিট্যান্স (Inheritance with Example) বর্ণনা কর। (রচনামূলক-০২)</strong></summary>

### উত্তর:

ইনহেরিট্যান্স (Inheritance): ইনহেরিট্যান্স অর্থ হচ্ছে উত্তরাধিকার সূত্রে পাওয়া। বাবার সম্পত্তি উত্তরাধিকার সূত্রে ছেলে পাবে এটাই স্বাভাবিক। ইনহেরিট্যান্স হচ্ছে একধরনের মেকানিজম, যেখানে চাইল্ড ক্লাস তৈরির সময় পেরেন্ট ক্লাসের বিহেভিয়ার ও প্রাপার্টিজ ধারণ করে। নিচের প্রোগ্রামে `Calculator` হচ্ছে পেরেন্ট ক্লাস, `SubCalculator` হচ্ছে চাইল্ড ক্লাস। `SubCalculator` ক্লাস `Calculator` ক্লাসের বৈশিষ্ট্য ধারণ করেছে। `my_calculator` হচ্ছে `SubCalculator` ক্লাসের অবজেক্ট, কিন্তু এর মাধ্যমে `Calculator` ক্লাসের মেম্বারসমূহও অ্যাক্সেস করা যাচ্ছে, একে ইনহেরিট্যান্স বলে।

---

### প্রোগ্রাম

```python
class Calculator:
    # Super Class

    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "It is impossible to divide by zero."


class SubCalculator(Calculator):
    # Child Class

    def square(self, x):
        return x * x

    def cube(self, x):
        return x * x * x


my_calculator = SubCalculator()

print("X + Y =", my_calculator.addition(60, 30))
print("X - Y =", my_calculator.subtraction(60, 30))
print("X * Y =", my_calculator.multiplication(60, 30))
print("X / Y =", my_calculator.division(60, 30))
print("Square of 9 =", my_calculator.square(9))
print("Cube of 5 =", my_calculator.cube(5))
```

### Output

```text
X + Y = 90
X - Y = 30
X * Y = 1800
X / Y = 2.0
Square of 9 = 81
Cube of 5 = 125
```

---

উপরের প্রোগ্রামে `Calculator` ক্লাস একটি **Super Class** এবং `SubCalculator` ক্লাস একটি **Child Class**। `SubCalculator` ক্লাস `Calculator` ক্লাসকে Inherit করেছে। তাই `SubCalculator`-এর অবজেক্ট `my_calculator` নিজস্ব `square()` ও `cube()` Method-এর পাশাপাশি `addition()`, `subtraction()`, `multiplication()` এবং `division()` Method-ও ব্যবহার করতে পারছে। পেরেন্ট ক্লাসের বৈশিষ্ট্য চাইল্ড ক্লাসে ব্যবহার করার এই প্রক্রিয়াকে **Inheritance** বলা হয়।

---

### Inheritance

`SubCalculator` Class, `Calculator` Class-এর সকল Public Method উত্তরাধিকার সূত্রে গ্রহণ করেছে। তাই `SubCalculator`-এর Object দিয়ে Parent Class-এর Method-গুলোও ব্যবহার করা সম্ভব হয়েছে। একে **Inheritance** বলা হয়।

---



### সংক্ষিপ্ত নোট (Process / Not write in exam)

- **Inheritance** অর্থ **উত্তরাধিকার সূত্রে Parent Class-এর বৈশিষ্ট্য গ্রহণ করা।**
- এটি **Code Reusability** বৃদ্ধি করে এবং একই কোড বারবার লেখার প্রয়োজন কমায়।
- Python-এ `class Child(Parent):` লিখে Inheritance তৈরি করা হয়।

</details>
<br>








<!--🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 -->
<details>
<summary><strong>📌 ইনহেরিট্যান্স এর প্রকারভেদ (রচনামূলক-০২) — অতিরিক্ত আলোচনা</strong></summary>

## ১। Single Inheritance

একটি পেরেন্ট ক্লাসের কমন বৈশিষ্ট্যসমূহ অন্য ক্লাসে ইনহেরিট করে কাজ করাকে **Single Inheritance** বলে।

### উদাহরণ

```python
class A:
    pass

class B(A):
    pass
```

---

## ২। Multilevel Inheritance

যদি একটি ডিরাইভড ক্লাসেরও আরও ডিরাইভড ক্লাস থাকে, তখন একে **Multilevel Inheritance** বলে।

### উদাহরণ

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

---

## ৩। Multiple Inheritance

একটি ক্লাস একই সাথে একাধিক ক্লাসকে ইনহেরিট করতে পারে। সেক্ষেত্রে ডিরাইভড ক্লাসের Parentheses-এর ভিতরে প্রতিটি Base Class-এর নাম উল্লেখ করতে হয়।

### উদাহরণ

```python
class ParentOne:
    pass

class ParentTwo:
    pass

class Child(ParentOne, ParentTwo):
    pass
```
---

## ৪। Hierarchical Inheritance

একটি Parent Class-এর একাধিক Child Class বিদ্যমান থাকলে তাকে **Hierarchical Inheritance** বলে।

### উদাহরণ

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass
```

---

## ৫। Hybrid Inheritance

যে পদ্ধতিতে দুই বা ততোধিক ইনহেরিট্যান্স পদ্ধতি ব্যবহার করা হয়, তাকে **Hybrid Inheritance** বলে।

### ধারণামূলক চিত্র

```text
      A
     / \
    B   C
     \ /
      D
```

এখানে `Single`, `Multiple` এবং `Multilevel` Inheritance-এর সমন্বয়ে **Hybrid Inheritance** গঠিত হয়েছে।

</details>
<br>











<!--🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 -->
<details>
<summary><strong>📌 Comprehensive-2: Code Explanation (try-except / Exception Handling)</strong></summary>

# 📝 `try-except` (Exception Handling)

```python
def division(self, x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "It is impossible to divide by zero."
```

### কোডের প্রতিটি অংশের নাম

| Code | নাম |
|------|-----|
| `def division(self, x, y):` | **Method Definition** |
| `try:` | **Try Block** |
| `return x / y` | **Division Operation** |
| `except ZeroDivisionError:` | **Except Block (Exception Handler)** |
| `ZeroDivisionError` | **Built-in Exception** |
| `return "It is impossible to divide by zero."` | **Error Message Return** |

---

### ব্যাখ্যা

উপরের কোডে `division()` নামে একটি **Method** তৈরি করা হয়েছে, যা দুটি সংখ্যাকে ভাগ করে। `try` Block-এর ভিতরে `x / y` এক্সিকিউট করার চেষ্টা করা হয়। যদি ভাগ করার সময় কোনো Error না হয়, তাহলে ফলাফল `return` করা হয়। কিন্তু `y`-এর মান `0` হলে Python `ZeroDivisionError` Exception তৈরি করে। তখন `except ZeroDivisionError` Block কার্যকর হয় এবং প্রোগ্রাম বন্ধ না হয়ে `"It is impossible to divide by zero."` মেসেজটি `return` করে। এই সম্পূর্ণ প্রক্রিয়াকে **Exception Handling** বলা হয়।

</details>