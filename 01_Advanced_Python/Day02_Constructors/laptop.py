class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram} GB")
        print(f"Price: ₹{self.price}")
        print("-" * 30)


l1 = Laptop("Dell", 16, 65000)
l2 = Laptop("HP", 8, 55000)
l3 = Laptop("Lenovo", 16, 70000)

l1.show_details()
l2.show_details()
l3.show_details()

