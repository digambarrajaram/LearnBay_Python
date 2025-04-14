class Product:
    def __init__(self,name,price,stock_quantity):
        self.name = name
        self.__price = price
        self.stock_quantity = stock_quantity

    def get_price(self):        #getter is used to return value of private member varibale outside the class 
        return self.__price

    def set_price(self,new_price):      #setter used to set the value of private member varibale inside the class 
         self.__price = new_price
    
    
    def sellProducat(self,quantity):
        if quantity <= self.stock_quantity:
            self.stock_quantity -= quantity
            print(f"Sold out {quantity} of product  {self.name}")
        else:
            print("Not enough stock available")


p1 = Product("Lapto",55000,10)

print("Price is", p1.get_price())  #Get the value of private member out side the class

p1.set_price(60000)     #Set the value to private member inside the class

print("New Price is", p1.get_price())  

print(f"Total quantity of present product is {p1.stock_quantity}")  #Old quantity
p1.sellProducat(7)
print(f"Total quantity after sold out of product {p1.stock_quantity}")  #New quantity



