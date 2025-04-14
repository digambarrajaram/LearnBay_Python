class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __add__(self,other):
        if isinstance(other,Product):   #isinstance(other,Product) :- isinstance(Product object ,Product object )
            return f"We can not add the two products into cart directly. Use the cart option to add one by one"
        elif isinstance(other,Cart):     #isinstance(other,Cart) :- isinstance(Cart object ,Cart object )
            other.add_product(self)     #other.add_product(self) :- other(Cart Object).add_product(Cart Method)(self(Product Object)) 
            return other
        return NotImplemented
    
    def __str__(self):
        return f"{self.name}"

class Cart:
    def __init__(self):
        self.products = []      #This is the empty array to store the multiple products

    def add_product(self,product):
        self.products.append(product)

    def display_cart(self):
        if not self.products:
            return "Your cart is empty"
        cart_details = "\n".join([str(product) for product in self.products])
        return f"This cart contains the products as : \n{cart_details}"
    

product1 = Product("Laptop",12000)
product2 = Product("Headphones",2000)
product3 = Product("watch",15000)
product4 = Product("watch",15000)

cart = Cart()

print(cart.display_cart())

cart = product1 + cart
cart = product2 + cart
cart = product3 + cart


print(cart.display_cart())


product4 = product2 + product3
print(f"{product4}")