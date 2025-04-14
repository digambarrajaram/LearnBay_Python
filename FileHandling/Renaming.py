import os
os.chdir("d:\\Python_LB\\FileHandling\\test\\")


old_file = r'd:\\Python_LB\\FileHandling\\test\\Demo1.txt'
new_file = r'd:\\Python_LB\\FileHandling\\test\\Backup_Demo1.txt'


#os.rename(old_file,new_file)

#if os.path.isfile(old_file):
    #os.rename(old_file,new_file)
#else:
    #print("File not present")


try:
    os.rename(old_file, new_file)        
except FileExistsError:
    print("File already exists")
except FileNotFoundError as e:
    print(f"Error: {e}")


#removeing the file
"""print(open('Test.txt','r').read())
os.remove('Test.txt')"""