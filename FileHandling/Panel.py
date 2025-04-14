import json,os,shutil           #Importing packages 
from datetime import datetime

os.chdir("d:\\Python_LB\\FileHandling\\test\\")     #Changing directory

DATA_FILE = 'products.json'
BACKUP_FOLDER = 'backup'

#We are making sure that backup folder do exists
os.makedirs(BACKUP_FOLDER,exist_ok=True)

#Method for backup
def create_backup():
    if os.path.exists(DATA_FILE):
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        backup_filename = f"{BACKUP_FOLDER}/product_backup_{timestamp}.json"
        shutil.copy(DATA_FILE,backup_filename)
        print(f"Backup got created : {backup_filename}")
    else:
        print("File not available to take backup")


#Method for reading the products data from the json file 
def read_products():
    try:
        if not os.path.exists(DATA_FILE):
            return[]
    
        with open(DATA_FILE,'r') as file:
            return json.load(file)

    except Exception as e:
        print(f"Error reading the product file {e} ")



#Method for writing the data into the products json file
def write_products(products):
    try:
        with open(DATA_FILE,'w') as file:
            json.dump(products,file,indent=4)
        print("Product data written successfully into the JSON file")
    except Exception as e:
        print(f"Error writting into file {e}")
    

#Method adding a new product
def add_new_product(products):
    print("\n 1) Add the new Product")
    try:
        product_id = int(input("Enter the Product ID : "))
        product_name = input("Enter the Product Name : ")
        product_price = float(input("Enter the Product Price : "))
        product_stock = int(input("Enter the Product Stock : "))
        
        new_product = {
            "id"  : product_id,
            "name"  : product_name,
            "price" : product_price,
            "stock" : product_stock
        }
        products.append(new_product)
        print("The new product got added !!")
    
    except ValueError:
        print("Invalid input. Product not added !!")



#Method to display all products
def display_products(products):
    if not products:
        print("\nNo products are available at the moment")
        return

    print("\nThe available products are as below : ")
    for product in products:
        print(f"\nThe Product ID : {product['id']} \nThe Product Name : {product['name']}\nThe Product price : {product['price']}\nThe Product stock : {product['stock']}\n====================================")



#Main method
def main():
    print("Loading the product data")
    product = read_products()
    display_products(product)

    user_choice = input("Do you want to add a new product? (YES/NO)").strip().lower()

    if user_choice in ("yes",'y'):
        create_backup()
        add_new_product(product)
        write_products(product)
    elif user_choice in ("no",'n'):
        pass
    else:
        print("!!!!!! Wrong option choosen !!!!!!")
        main()

main()

