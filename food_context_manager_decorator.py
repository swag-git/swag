from contextlib import contextmanager


@contextmanager
def food_context_manager(data):
    print(f"Enter: {data}")
    yield data
    print(f"Exit: {data}")


with food_context_manager({'banana': 'fruit'}) as data:
    data['carrot'] = 'veggie'
    print(f"Inside the context: {data}")

print(f"Outside the context: {data}")
