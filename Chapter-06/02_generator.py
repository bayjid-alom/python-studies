# Generator
def square_numbers(n):
    for i in range(1, n + 1):
        yield i * i


a = square_numbers(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))