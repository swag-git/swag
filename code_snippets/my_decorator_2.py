def my_decorator(func):
    def new_func():
        return func() + "!!!!!"
    return new_func


# using a decorator tag
@my_decorator
def hello_world():
    return "Hello, world"


print(hello_world())
