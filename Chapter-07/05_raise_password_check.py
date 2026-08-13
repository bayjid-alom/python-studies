password = input("Enter your password : ")

if len(password) < 8:
    raise ValueError("Password must be at least 8 characters!")

print("Password is valid.")


"""
Output-01:
Enter your password : bayjid35
Password is valid.


Output-02:
Enter your password : Bayjid5
Traceback (most recent call last):
  File "C:\Python-Programming\Chapter-07\05_raise_password_check.py", line 4, in <module>
    raise ValueError("Password must be at least 8 characters!")
ValueError: Password must be at least 8 characters!

"""
