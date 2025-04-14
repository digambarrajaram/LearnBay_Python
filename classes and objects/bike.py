class Bike:          #class declaration
    name = ""       #class attributes
    wheels = 2
    gear = 4
    brand = ""



bike1 = Bike()  #object creation 

bike1.name = 'Yamaha 120 CC'  # We are assign the values to attributes using object of class Bike
bike1.brand = 'Yamaha'

print(f"Name of bike 1 is {bike1.name} and brand is {bike1.brand} having {bike1.gear} gears")


bike2 = Bike()
bike2.name = 'Yamaha 200 CC'
bike2.gear = 2
bike2.brand = 'Yamaha'


print(f"Name of bike 2 is : {bike2.name} and wheels are : {bike2.brand} having  : {bike2.gear} gears")

print(bike1)



'''class Bike:
    def __init__(self, name, brand):
        self.name = name  # Attribute for the bike's name
        self.brand = brand  # Attribute for the bike's brand

    # Define the __str__ method to represent the object as a string
    def __str__(self):
        return f"Bike(Name: {self.name}, Brand: {self.brand})"

# Creating an object of the Bike class
bike1 = Bike("Mountain Bike", "Trek")

# Printing the object
print(bike1)'''