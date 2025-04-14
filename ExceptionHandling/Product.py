def order():
    try:
        price = float(input("Enter price of the product : "))
        quantity = float(input('Enter Quantity you want : '))

        if price < 0 or quantity < 0:
            raise ValueError("Price and Quantity value should be in positive")
        
        total_price = price*quantity
        print(f"Total price of the product is :{total_price}")

    except ValueError as ep:
        print(f"The user invalid input : {ep}")

#order()


def product():
    try:
        stock = {"Laptop":10,"Mobile":0,"headphones":50}

        buy_product = input("Enter name of product you want to buy :")

        if buy_product not in stock:
            raise ValueError("Product you entered is not available in the inventory")
        
        if stock[buy_product] ==  0:
            raise ValueError("Out of stock")
        
        print(f"The product {buy_product} is avalable and {stock[buy_product]} units are present to purchase")

    except ValueError as e:
        print(e)

product()





