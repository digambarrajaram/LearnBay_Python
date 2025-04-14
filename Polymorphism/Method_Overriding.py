class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def emp_details(self):
        print(f" The employee name is {self.name} with Salary {self.salary}")

    
class Manager(Employee):
    def __init__(self, name, salary,dept,project):
        super().__init__(name, salary)
        self.dept = dept
        self.project = project

    def emp_details(self):
        super().emp_details()
        print(f" The employee name is {self.name} with Salary {self.salary} work in department {self.dept} and assigned with project {self.project}")


emp = Manager("Ravi",40000,"IT","Google")
emp.emp_details()