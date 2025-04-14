class Product:
    def __init__(self,name,price):  #constructor
        self.name = name
        self.price = price

    def display(self):    #Mentod of parent class
        print(f"Producat with name: '{self.name}' is priced at value INR: '{self.price}'")

class Clothing(Product):
    def __init__(self, name, price,size):
        super().__init__(name, price)
        self.size = size

    def display(self):
        super().display()
        print(f"The product size is {self.size}")


class Watch(Product):
    def __init__(self, name, price,brand):
        super().__init__(name, price)
        self.brand = brand


    def display(self):
        super().display()
        print(f"The product brand is {self.brand}")



t_Shirt = Clothing('nike',2000,'S')
t_Shirt.display()


smart_watch = Watch('Smart X Series Watch',15000,'Titan')
smart_watch.display()

