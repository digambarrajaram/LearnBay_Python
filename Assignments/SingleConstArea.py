#4. area of circle,sqaure,rectangle using single constructor
print("\n Program to find area of circle,sqaure,rectangle using single constructor")
class Shape:
    def __init__(self,l,b,h,r):
        self.l , self.b =  l , b
        self.h = h
        self.r = r

    def area_of_circle(self):
        return 3.142*self.r*self.r
    def area_of_rect(self):
        return self.l*self.b*self.h
    def area_of_square(self):
        return self.l*self.b

shapeObj = Shape(10,10,5,2)
print(f" Area of circle is {shapeObj.area_of_circle()}")
print(f" Area of Rectangle is {shapeObj.area_of_rect()}")
print(f" Area of Square is {shapeObj.area_of_square()}")