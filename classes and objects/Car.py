class Car:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

    def carType(self):
        print(f"I have car {self.name} which is of brand {self.brand}")


car1 = Car('Honda City','Honda')
car2 = Car('Nano','Tata')
car1.carType()
car2.carType()


