import os 

print(os.getcwd()) 
os.chdir("d:\\Python_LB\\FileHandling\\test\\")
print(os.getcwd()) 

with open('Demo1.txt','r') as fp:       #read the first line of file
    line = fp.readline()
    print(line)


with open('Demo1.txt','r') as fp:       #read the lines of the file based on range 
    for i in range(4):
        print(fp.readline())

    for i in range(4):
        print(fp.readline().strip())


with open('Demo1.txt','r') as fp:       #read the lines of the file based on range 
    for i in range(4):
        print(fp.readline().strip())    #strip is used to trim or remove spaces 


with open('Demo1.txt','r') as fp:       #to print first and last line of the program
    fLine = fp.readline()
    print(fLine)
    
    for lLine in fp:        # to print last line of the file
        pass                # it will pass all iteration till last line of the file or pass till last value of object/array
    print(lLine)            # print last line



print('=============================================')
#print(open('Demo1.txt','r').read())
with open('Demo1.txt','r') as fp:
    print(fp.read())


print("\n\n\n\n\n\n")
def read_file(filename):
    try:
        with open(filename,'r') as file:
            data = file.read()
            print("Below is the file content")
            print(data)
            file.close()
    except FileNotFoundError as fnfe:
        print("Error is -> ",fnfe)
    except IOError as io:
        print(io)

filename = 'Demo1.txt'
read_file(filename)
    



