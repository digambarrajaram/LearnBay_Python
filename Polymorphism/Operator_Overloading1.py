class CustomClass:
    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        if isinstance(self.value,int) and isinstance(other.value,int):
            #print("self.Value -> ",self.value," other.value -> ",other.value)
            #print(CustomClass(self.value + other.value ))
            return CustomClass(self.value + other.value )  
        elif isinstance(self.value,str) and isinstance(other.value,str):
            return CustomClass(self.value + other.value )
        return NotImplemented
    
    def __str__(self):
        return str(self.value)


num1 = CustomClass(20)
num2 = CustomClass(30)

result = num1 + num2     # num1.__add__(num2)       #First value is always self and second is other : num1 is self.value and num2 is other.value
print(f" Sum of two numbers --> {result}")

str1 = CustomClass("Python")
str2 = CustomClass("Lanugage")

str_result = str1 + str2    #str1.__add__(str2)
print(f"String result --> {str_result}")

