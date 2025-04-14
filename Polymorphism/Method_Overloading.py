class Calculator:
    def add(self,a=1,b=1,c=1):    # default arguments, If no default variable values assigned and if we call method without parameter then it will throw a error
        return a + b + c 
    
obj = Calculator()

print(obj.add())
print(obj.add(10))
print(obj.add(10,20))
print(obj.add(10,20,30))


class Employee:
    def emp_info(self,*args):
        if len(args) == 1:
            print(f"The employee argument is : {args[0]}")
        elif len(args) == 2:
            print(f"The employee arguments are : {args[0]} and {args[1]}")
        else:
            print(f"Invalid number of arguments")
        
emp = Employee()

emp.emp_info("Ravi")
emp.emp_info("IT",3000,20)
emp.emp_info("TV",3000,)