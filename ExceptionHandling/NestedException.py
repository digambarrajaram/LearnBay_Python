class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock


def purchase_product():
    try:
        products = {
            "Mobile" : Product("Mobile",30000,6),
            "Laptop" : Product("Laptop",50400,0),
            "Watch"  : Product("Watch",300,20)
        } 

        buy_product = input("Enter the product you want to buy : ")

        try:
            if buy_product not in products:
                raise ValueError("Entered product not present in inventory")
            
            product = products[buy_product]

            try:
                quantity = int(input("Enter quantity you want to buy"))
                if quantity<= 0:
                    raise ValueError("Quanity must be greater than 0")
                
                if quantity > product.stock:
                    raise ValueError(f" sorry you are going out of inventory available. We have only {product.stock} for name {product.name}")
                
                total_price = product.price * quantity
                print(f"The total price for {quantity} of product {product.name} is INR. {total_price}")
                product.stock = product.stock - quantity
                print(f"Now you have {product.stock} of product {product.name} left in inventory")

            except ValueError as ep:
                print(f" Quantity error as {ep}")
        
        except ValueError as ep:
            print(f" Product error : {ep}")
    
    except Exception as ep:
        print(f" Unexcpted constion Error is : {ep}")


purchase_product()
