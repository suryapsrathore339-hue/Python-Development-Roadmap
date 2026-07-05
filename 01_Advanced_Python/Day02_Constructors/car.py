class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def show_details(self):
        print("Car:",self.brand,"| Model:",self.model,"| Price:",self.price)

c1=Car("Toyota","Corolla",2000000)
c2=Car("Honda","City",1500000)
c3=Car("Hyundai","i20",1200000)
c4=Car("Maruti","Suzuki_500",500000)

c1.show_details()
c2.show_details()
c3.show_details()
c4.show_details()
