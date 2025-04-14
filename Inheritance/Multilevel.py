class Product:
    def __init__(self,name,price):  #constructor
        self.name = name
        self.price = price

    def display(self):    #Mentod of parent class
        print(f"Producat with name: '{self.name}' is priced at value INR: '{self.price}'")

class PhysicalProduct(Product):
    def __init__(self, name, price,weight):
        super().__init__(name, price)
        self.weight = weight

    def display(self):
        super().display()
        print(f"Producat weight is '{self.weight}' KG")

    
class EleProd(PhysicalProduct):
    def __init__(self, name, price, weight,warranty):
        super().__init__(name, price, weight)
        self.warranty = warranty

    def display(self):
        super().display()
        print(f"Producat name: '{self.name}' is priced at value INR: '{self.price}' of weight '{self.weight}' KG and warranty is '{self.warranty}'")



eleProduct = EleProd('HP',35000,5,2027)

eleProduct.display()
