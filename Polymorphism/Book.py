class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def __add__(self,other):
        if isinstance(other,Book):
            return Book(self.title +" & "+other.title, self.pages + other.pages)
        return NotImplemented

    def __str__(self):
        return f"Book : {self.title}, Pages : {self.pages}"


book1 = Book("Python Basics", 200)
book2 = Book("Advanced Python", 300)

book3 = book1 + book2

print(book3)