from abc import ABC, abstractmethod
class Product(ABC):

    @abstractmethod
    def Display_Product_Info(self):
        pass

    @abstractmethod
    def Calculate_Price(self):
        pass

    def display(self):
        print("This my base class display method")


class PhysicalProduct(Product):
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

    def Display_Product_Info(self):     #Method overriding
        return f"Product with name {self.name} is having the weight of {self.weight} KG"
    
    '''def Calculate_Price(self):
        pass'''

class Electronics(PhysicalProduct):
        
    def Calculate_Price(self):
        shipping_cost = self.weight * 10
        total = shipping_cost + self.price
        return f"Total price with weight charges {total}"
    
laptop = Electronics('HP',35000,5)

#laptop = PhysicalProduct('HP',35000,5)


print(laptop.Display_Product_Info())
print(laptop.Calculate_Price())
laptop.display()




#create 1 class as Employee in which we need to do following operations
#class variables
# -name
# -salary
# -bonus
# -leaves
# -dept

# Hint 
# class Employee as abstract 
# class Salary(Employee) --> create the object of this class 
# in this class we will calculate all the salary after bonus and salary after leaves taken and display method also

#Questions 
# a) calculate the slaray of the employee and calculate the new salaray of the employee after having bonus
# b) calculate the strict_salary (means deduacting the number of leaves taken that month ) (assume salary_per_day = 1000)
# strict_salary = salary - (salary_per_day * leaves)
# c) display method should print all the class variables



