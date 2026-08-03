print("===========| Decorator |===========")


def decorator(task):
    def wrapper():
        print("Starting the task...")
        task()
        print("Task completed successfully!")

    return wrapper


def study_python():
    print("Learning Python Decorators.")


decorated_task = decorator(study_python)
decorated_task()


print("===========| Iterator |===========")

list = iter([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
for i in list:
    if i % 2 == 0:
        print(i, "is an even number.")
    else:
        print(i, "is an odd number.")
 

print("===========| Generator |===========")


def square_number(n):
    for i in range(1, n + 1):
        square = i**2
        yield square


x = square_number(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
