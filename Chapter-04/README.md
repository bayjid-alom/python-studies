## 🧩 Object-Oriented Programming (OOP)

> **Chapter Name:** **BASICS OF OOP**
---




## 📖 OOP কী?

> **OOP (Object-Oriented Programming)** হলো এমন একটি **Programming Paradigm** যেখানে **Class** এবং **Object** ব্যবহার করে বাস্তব জীবনের বিভিন্ন জিনিসকে মডেল করে প্রোগ্রাম তৈরি করা হয়।
---




## ✔️ Characteristics of OOP (OOP-এর বৈশিষ্ট্য)

| No. | Characteristic | Meaning |
|:---:|----------------|---------|
| 01 | **Class** | Blueprint |
| 02 | **Object** | Instance |
| 03 | **Encapsulation** | Data Hiding |
| 04 | **Abstraction** | Hide Complexity |
| 05 | **Inheritance** | Code Reuse |
| 06 | **Polymorphism** | Multiple Forms |
| 07 | **Message Passing** | Communication |
| 08 | **Dynamic Binding** | Runtime Method Selection |
| 09 | **Open Recursion** | Self Method Call |
---
<br>



## 🏛️ OOP-এর ৪টি Pillars

- 🔒 **Encapsulation**
- 🎭 **Abstraction**
- 👨‍👩‍👦 **Inheritance**
- 🔄 **Polymorphism**
---




## ✔️ Special Methods (Magic / Dunder Methods)

### 🔹 Magic Method

> Python-এ যেসব **Special Method**-এর নামের **শুরু ও শেষে Double Underscore (`__`)** থাকে, সেগুলোকে **Magic Method** বলা হয়।

📌 উদাহরণ

```python
__init__()
__str__()
__len__()
__add__()
```
--- 
<br>




### 🔹 Dunder Method

> **Dunder** অর্থ **Double UNDERscore**।

যেসব Method-এর **শুরু এবং শেষে `__` থাকে**, সেগুলোকে **Dunder Method**-ও বলা হয়।

📌 উদাহরণ

```python
__init__
```

পড়তে হবে:

> **Dunder Init**

আরও উদাহরণ:

- Dunder Str
- Dunder Len
- Dunder Add
- Dunder Eq

> **সংক্ষেপে:** Python-এ **Magic Method** এবং **Dunder Method** একই জিনিস।
---
<br>




## ✔️ Arithmetic Magic Methods

| Magic Method | Operator | Purpose |
|--------------|:-------:|---------|
| `__add__(self, other)` | `+` | Addition |
| `__sub__(self, other)` | `-` | Subtraction |
| `__mul__(self, other)` | `*` | Multiplication |
| `__truediv__(self, other)` | `/` | Division |
| `__floordiv__(self, other)` | `//` | Floor Division |
| `__mod__(self, other)` | `%` | Modulus |
| `__pow__(self, other)` | `**` | Exponentiation |

---
<br>




## 🔄 Type Conversion Magic Methods

- `__int__(self)` → **Integer**-এ রূপান্তর করে *(পূর্ণসংখ্যায় রূপান্তর করে)*।
- `__float__(self)` → **Float**-এ রূপান্তর করে *(দশমিক সংখ্যায় রূপান্তর করে)*।
- `__str__(self)` → **String**-এ রূপান্তর করে *(স্ট্রিং হিসেবে প্রকাশ করে)*।
- `__bool__(self)` → **Boolean**-এ রূপান্তর করে *(True বা False নির্ধারণ করে)*।
- `__complex__(self)` → **Complex Number**-এ রূপান্তর করে *(জটিল সংখ্যায় রূপান্তর করে)*।
- `__bytes__(self)` → **Bytes**-এ রূপান্তর করে *(বাইট অবজেক্টে রূপান্তর করে)*।

---


### 📝 Summary

- ✔️ OOP = Class ও Object ভিত্তিক Programming Paradigm।
- ✔️ OOP-এর ৯টি প্রধান বৈশিষ্ট্য রয়েছে।
- ✔️ OOP-এর ৪টি মূল Pillars হলো Encapsulation, Abstraction, Inheritance এবং Polymorphism।
- ✔️ `__name__` ধরনের Method-কে **Magic Method** বা **Dunder Method** বলা হয়।
- ✔️ Magic Method ব্যবহার করে Operator Overloading ও Type Conversion করা যায়।