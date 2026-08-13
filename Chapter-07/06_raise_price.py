price = float(input("Enter the price: "))

if price <= 0:
    raise ValueError("Price must be greater than zero!")

print("Price is valid.")


"""
Output-01:
Enter the price: 100
Price is valid.


Output-02:
Enter the price: -200
Traceback (most recent call last):
  File "C:\Python-Programming\Chapter-07\06_raise_price.py", line 4, in <module>
    raise ValueError("Price must be greater than zero!")
ValueError: Price must be greater than zero!

"""