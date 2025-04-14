from abc import ABC,abstractmethod
class Employee():
    def __init__(self,name,salary,bonus,leaves,dept):
        self.name = name
        self.salary = salary
        self.bonus = bonus
        self.leaves = leaves
        self.dept = dept

    @abstractmethod
    def Emp_Salary(self):
        pass

    @abstractmethod
    def Emp_Salary_With_Bonus(self):
        pass

    @abstractmethod
    def Emp_Strict_Salary(self,salary_per_day):
        pass

    @abstractmethod
    def display(self):
        pass

class Salary(Employee):
    def __init__(self, name, salary, bonus, leaves, dept, salary_per_day):
        super().__init__(name, salary, bonus, leaves, dept)
        self.salary_per_day = salary_per_day


    def Emp_Salary(self):
        return self.salary

    def Emp_Salary_With_Bonus(self):
        return self.salary+self.bonus

    def Emp_Strict_Salary(self):
        return (self.salary - (self.salary_per_day * self.leaves))
    
    def display(self):
        print(f"Employee details as shown below \nName : {self.name}\nSalary : {self.salary}\nBonus : {self.bonus}\nLeaves : {self.leaves}\ndept : {self.dept}\nSalary Per Day : {self.salary_per_day}")
    

emp1 = Salary('Digambar',70000, 50000 , 3 , 'IT', 1000)

print("Salary of employee is :",emp1.Emp_Salary())
print("Salary of employee with bonus is :",emp1.Emp_Salary_With_Bonus())
print("Strict salary of employee is :",emp1.Emp_Strict_Salary())
emp1.display()


