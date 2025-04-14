class InvalidAge(Exception):
    pass

def vote():
    age = int(input("Enter your age : "))
    try:
        if age < 18:
            raise InvalidAge("Your age is below 18")
        print("You can vote ")
    except InvalidAge as i:
        print(i)
    finally:
        print("Everyone should vote above 18 years !!")
    
vote() 