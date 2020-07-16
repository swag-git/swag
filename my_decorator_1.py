def my_decorator(func):
    def new_func():
        return func() + '!!!!!!'
    return new_func


# not using a decorator tag demands an explicit call to *my_decorator*
def hello_world():
    return "Hello, world"


# *my_decorator* receives the function to decorate
# it returns a new function with extended behavior
# the function is stored in the variable hello
hello = my_decorator(hello_world)

# *hello* will be a function that wraps *hello_world*
# the extended behavior is to add '!!!!!!' to *hello_world*
print(hello())
