class Product:
    def __init__(self,id,name):  #constructor
        self.id = id
        self.name = name

    def display(self):    #Mentod of parent class
        print(f"Id of product is {self.id} and name of product is {self.name}")


class Product_Type_1(Product):
    def __init__(self, id, name,count,category):
        super().__init__(id, name)
        self.count = count
        self.category = category

    def display(self):
        super().display()
        print(f"The product id , Name, Count and Category is : {self.id}, {self.name}, {self.count} and {self.category}")


class Product_Type_1A(Product_Type_1):
    def __init__(self, id, name, count, category,price):
        super().__init__(id, name, count, category)
        self.price = price

    def display(self):
        super().display()
        print(f"The Total price is {self.count * self.price}.\nThe product id , Name and Category is : {self.id}, {self.name} and {self.category}")


firstProduct = Product_Type_1A(1,"Amul",50,"butter",30)
firstProduct.display()


print('----------------------------------------------------------------------------')
class Product_Type_2(Product):
    def __init__(self, id, name,count,category):
        super().__init__(id, name)
        self.count = count
        self.category = category

    def display(self):
        super().display()
        print(f"The product id , Name, Count and Category is : {self.id}, {self.name}, {self.count} and {self.category}")


class Product_Type_1B(Product_Type_2):
    def __init__(self, id, name, count, category,price):
        super().__init__(id, name, count, category)
        self.price = price

    def display(self):
        super().display()
        print(f"The Total price is {self.count * self.price}.\nThe product id , Name and Category is : {self.id}, {self.name} and {self.category}")

secondProduct = Product_Type_1A(1,"Amul",90,"Milk",10)
secondProduct.display()


print('----------------------------------------------------------------------------')
class Product_Type_3(Product):
    def __init__(self, id, name,count,category):
        super().__init__(id, name)
        self.count = count
        self.category = category

    def display(self):
        super().display()
        print(f"The product id , Name, Count and Category is : {self.id}, {self.name}, {self.count} and {self.category}")

tProduct = Product_Type_3(1,"Amul",50,"choco")
tProduct.display()

