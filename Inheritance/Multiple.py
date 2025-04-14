#Parent class/base class/supper class 1
class Product:
    def __init__(self,name,price):  #constructor
        self.name = name
        self.price = price

    def display_Info(self):    #Mentod of parent class
        print(f"Producat with name: {self.name} is priced at value INR: {self.price}")

#Parent class/base class/supper class 2
class Discount:
    def __init__(self,discount):  #constructor
        self.discount = discount

    def apply_discount(self,price):
        return price *(1- self.discount)


#Child class with inheritated propeties of parent class 1 and 2
class ProductSale(Product,Discount):
    def __init__(self, name, price,discount):
        Product.__init__(self,name,price)
        Discount.__init__(self,discount)

    def all_discouunt(self):
        discounted_values = self.apply_discount(self.price)
        print(f"The procuct {self.name} has price {self.price} with {self.discount*100} % discount.\nTotal discounted amount is {discounted_values}")
        

product_item = ProductSale('HP',55000,0.30)
product_item.all_discouunt()





