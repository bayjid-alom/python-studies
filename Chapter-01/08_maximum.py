def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c


num1 = int(input("Enter first value = "))
num2 = int(input("Enter second value = "))
num3 = int(input("Enter third value = "))

result = maximum(num1, num2, num3)
print("Maximum value is = ", result)


"""
Enter first value = 40
Enter second value = 50
Enter third value = 30
Maximum value is =  50
"""
