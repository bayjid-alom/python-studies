def check_positive(number):
    if number < 0:
        raise ValueError("Please enter a positive number!")
    print("Valid number")


number = int(input("Enter a number: "))
check_positive(number)


"""
Output-01:
Enter a number: 20
Valid number



Output-02:

Enter a number: -10
Traceback (most recent call last):
  File "C:\Python-Programming\Chapter-07\04_positive_number.py", line 8, in <module>
    check_positive(number)
    ~~~~~~~~~~~~~~^^^^^^^^
  File "C:\Python-Programming\Chapter-07\04_positive_number.py", line 3, in check_positive
    raise ValueError("Please enter a positive number!")
ValueError: Please enter a positive number!

"""
