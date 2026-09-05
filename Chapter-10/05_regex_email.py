import re


def isValid(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


email = input("Enter your email: ")

if isValid(email):
    print("Valid Email")
else:
    print("Invalid Email")
