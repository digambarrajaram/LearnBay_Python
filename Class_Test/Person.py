class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old")

class Student(Person):
    def __init__(self,name,age,student_id): 
        super().__init__(name,age)       
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"My student id is {self.student_id}")


std1 = Student("Akash",24,101)
std1.greet()


     