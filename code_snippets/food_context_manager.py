class FoodContextManager:
    def __init__(self, data):
        self.data = data

    def __enter__(self):
        print(f"Enter: {self.data}")
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exit: {self.data}")


with FoodContextManager({'banana':'fruit'}) as data:
    data['carrot'] = 'veggie'
    print("Inside context inserted: \'carrot\':\'veggie\'")

print(f"Outside context: {data}")
