def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a positive number: "))

if n < 0:
    print("You entered a negative number. Please try again.")
    exit(0)

print(f"The factorial of {n} is: {factorial(n)}")