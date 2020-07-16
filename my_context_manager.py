class MyContextManager:
    def __enter__(self):
        print("Enter!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit!")


with MyContextManager():
    print("Inside the context block!")



