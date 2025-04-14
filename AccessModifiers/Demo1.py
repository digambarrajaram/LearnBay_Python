class Employee:
    def __init__(self,name,age,salary):
        self.name = name            #Public access modifier 
        self.__age = age            #Private access modifier 
        self._salary = salary       #Protected access modifier

    def Employee_Details(self):
        print(f"The employee name is {self.name} whose age is {self.__age} and taing salary of INR. {self._salary}")


emp1 = Employee("Ravi",34,30000)

emp1.Employee_Details()


print(emp1.name)        #Public is accessible outside the class with object 
#print(emp1.__age)      #Private is not accessible outside the class 
#Name mangling :- private access modifiers can accessible outside the class it is use in rarest casees and not a good practice to use 
#Example for Name mangling
print(emp1._Employee__age)  # now it is accessible outside the class. Obj._ClassName__VarName

print(emp1._salary)     #Protected is accessible in child class with object 


