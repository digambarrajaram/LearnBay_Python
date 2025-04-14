class Room:     #Room class defination 
    l,b,h = 0.0,0.0,0.0

    def calculate_area(self):
        print(self.l)
        area = self.l*self.b*self.h
        print("area is -> ",area)

room1 = Room() #Object of Room() class 
room1.l = 40.0
room1.b = 90.3
room1.h = 20.4
room1.calculate_area()


room2 = Room()
room2.l = 3.0
room2.b = 50.3
room2.h = 10.4
room2.calculate_area()









 
