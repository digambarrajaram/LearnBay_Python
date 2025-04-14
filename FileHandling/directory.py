import os                                           #We are importing the module to handle the file and directory operations
print(os.getcwd())                                  #getcwd() :- to know the current working directory

'''path = "d:\\Python_LB\\FileHandling\\test\\"
os.chdir(path) '''
os.chdir("d:\\Python_LB\\FileHandling\\test\\")     #changing the curerent direcotry
print(os.getcwd())          

fp = open("Demo1.txt","w")                          # Open new file :- creating new file with w mode
fp.write("Hello, This is demo1 file")               #writing data into file
fp.close()                                          #closing the file 


#listing files present in directory/current working directory
os.chdir("d:\\Python_LB\\FileHandling\\")     #changing the curerent direcotry
print(os.getcwd()) 
print(os.listdir())


#just check is file is present in cwd
print(os.path.isfile('Demo1.txt'))

