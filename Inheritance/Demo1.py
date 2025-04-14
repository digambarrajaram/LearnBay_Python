#Parent class/base class/supper class
class Product:
    def __init__(self,name,price):  #constructor
        self.name = name
        self.price = price

    def Display_Info(self):    #Mentod of parent class
        print(f"Producat with name: {self.name} is priced at value INR: {self.price}")


#child/derived/subclass class
class Electronic(Product):   # class declaration with inheritance 
    def __init__(self,name,price,warranty):  #child class constructor
        super().__init__(name,price)        #calling or assign values to parent class constructor
        self.warranty = warranty 


    def Display_Info(self):    #Mentod of child class 
        super().Display_Info()
        print(f"Producat with name: {self.name} is priced at value INR: {self.price} with Warranty till year {self.warranty}")


LedTv = Electronic('TV',23000,2027)
LedTv.Display_Info()

washing_machine = Electronic('Samsung',30000,2030)

washing_machine.Display_Info()