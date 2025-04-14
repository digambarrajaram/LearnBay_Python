import os 

#print(os.getcwd()) 
os.chdir("d:\\Python_LB\\FileHandling\\test\\")
#print(os.getcwd()) 


product_data = [

    'Name : Laptop',
    '\nPrice : 45000',
    '\nBrand : Samsung',
    '\nCity : Mumbai'
]


fp = open('product.txt','w')
fp.writelines(product_data)
fp.close()

fp = open('product.txt','r')
print(fp.read())
fp.close()