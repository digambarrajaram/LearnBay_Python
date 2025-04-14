from abc import ABC, abstractmethod
class Product(ABC):

    @abstractmethod
    def Display_Product_Info(self):
        pass

    @abstractmethod
    def Calculate_Price(self):
        pass


class PhysicalProduct(Product):
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

    def Display_Product_Info(self):     #Method overriding
        return f"Product with name {self.name} is having the weight of {self.weight} KG"
    
    def Calculate_Price(self):
        shipping_cost = self.weight * 10
        total = shipping_cost + self.price
        return f"Total price with weight charges {total}"
    
laptop =PhysicalProduct('HP',35000,5)

print(laptop.Display_Product_Info())
print(laptop.Calculate_Price())