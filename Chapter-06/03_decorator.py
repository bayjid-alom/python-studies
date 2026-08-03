# Decorator
def my_decorator(func):
    def decorate():
        print("-----------")
        func()
        print("===========")

    # under my_decorator()
    return decorate


def our_country():
    print("Bangladesh")


decorated_function = my_decorator(our_country)
decorated_function()
