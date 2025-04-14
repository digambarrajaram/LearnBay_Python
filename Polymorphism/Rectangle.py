class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def __add__(self,other):
        if isinstance(self.l,(int,float)) and isinstance(other.l,(int,float)) and isinstance(self.b,(int,float)) and isinstance(other.b,(int,float)):
            return Rectangle(self.l + other.l , self.b + other.b)
        return NotImplemented
    
    def __eq__(self,other):
        if isinstance(self.l,(int,float)) and isinstance(other.l,(int,float)) and isinstance(self.b,(int,float)) and isinstance(other.b,(int,float)):
            rect1 = self.l * self.b
            rect2 = other.l * other.b
            return rect1 == rect2       # return  f"Rectangle {self.l * self.b == other.l * other.b}"
            
        return NotImplemented
               
    def __str__(self):
        return f"Rectangle({self.l},{self.b})"
    

rect1 = Rectangle(10, 5)
rect2 = Rectangle(4, 6)

rect3 = rect1 + rect2
print(rect3)   # Rectangle: Length=14, Width=11



rect4 = Rectangle(6, 6)
rect5 = Rectangle(9, 4)

result = rect4 == rect5

print(result)  # True (Area = 36)