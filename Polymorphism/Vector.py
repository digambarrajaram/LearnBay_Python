class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        if isinstance(other,Vector):
            #print(f"self-->{self},other-->{other}")
            return Vector(self.x + other.x , self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f" Vector({self.x},{self.y})"

vector1 = Vector(10,20)
vector2 = Vector(30,30)

new_vector = vector1 + vector2      #calling of __add__() method 

print(f"Result of combined vector objects are : {new_vector}")
