class Number:
    def __init__(self, value):
        # Constructor to initialize the number
        self.value = value

    def __add__(self, other):
        # Overloads the + operator
        return Number(self.value + other.value)

    def __sub__(self, other):
        # Overloads the - operator
        return Number(self.value - other.value)

    def __mul__(self, other):
        # Overloads the * operator
        return Number(self.value * other.value)

    def __truediv__(self, other):
        # Overloads the / operator (true division)
        return Number(self.value / other.value)

    def __floordiv__(self, other):
        # Overloads the // operator (floor division)
        return Number(self.value // other.value)

    def __mod__(self, other):
        # Overloads the % operator (modulus)
        return Number(self.value % other.value)

    def __pow__(self, other):
        # Overloads the ** operator (exponentiation)
        return Number(self.value ** other.value)

    def __eq__(self, other):
        # Overloads the == operator (equality comparison)
        return self.value == other.value

    def __ne__(self, other):
        # Overloads the != operator (inequality comparison)
        return self.value != other.value

    def __gt__(self, other):
        # Overloads the > operator (greater than)
        return self.value > other.value

    def __lt__(self, other):
        # Overloads the < operator (less than)
        return self.value < other.value

    def __ge__(self, other):
        # Overloads the >= operator (greater than or equal to)
        return self.value >= other.value

    def __le__(self, other):
        # Overloads the <= operator (less than or equal to)
        return self.value <= other.value

    def __str__(self):
        # Defines how the object is printed
        return f"Number({self.value})"


'''n1 = Number(int(input("Enter your 1st number : ")))
n2 = Number(int(input("Enter your 2nd number : ")))'''


n1 = Number(10)
n2 = Number(3)

print(n1 + n2)     # Number(13)
print(n1 - n2)     # Number(7)
print(n1 * n2)     # Number(30)
print(n1 / n2)     # Number(3.333...)
print(n1 // n2)    # Number(3)
print(n1 % n2)     # Number(1)
print(n1 ** n2)    # Number(1000)
print(n1 == n2)    # False
print(n1 != n2)    # True
print(n1 > n2)     # True
print(n1 < n2)     # False
print(n1 >= n2)    # True
print(n1 <= n2)    # False