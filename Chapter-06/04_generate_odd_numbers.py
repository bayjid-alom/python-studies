# Using genarator - Python TB Page : 115 - Program:2


def oddNumbers(num):
    for i in range(num):
        if i % 2 != 0:
            yield i


result = oddNumbers(100)
for i in result:
    print(i, end=" ")
