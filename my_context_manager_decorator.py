from contextlib import contextmanager

# the decorator builds __enter__ and __exit__ functions for us


@contextmanager
def my_context_manager():
    print("Enter!")
    yield
    print("Exit!")


with my_context_manager():
    print("Inside the context!")
