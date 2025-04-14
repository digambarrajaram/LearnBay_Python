import os
os.chdir(r"D:\Python_LB\Assignments")

aw = open('A.txt','w')
aw.write("Hello,\nThis is A file's content")
aw.close()

"""ar = open('A.txt','r')
print(ar.read())
ar.close()"""

#ar = open('A.txt','r')
#data = ar.readlines()
#print(len(data))
#print(data)

#for i in range(len(open('A.txt','r').readlines())):  
#with open('B.txt','a') as bw:
#    with open('A.txt','r') as ar:       
#        bw.write(line)
#        print(line)


with open('B.txt','w') as bw:     #Use mode as 'a' if you want to copy content of file to existing file
    with open('A.txt','r') as ar:       
        bw.write(ar.read())
        ar.close()
        bw.close()
print("Printing file B content after copying content from A file\n",open('B.txt','r').read())

#Rename the file A.txt as A_Backup.txt
os.rename(r"D:\Python_LB\Assignments\A.txt",r"D:\Python_LB\Assignments\A_Backup.txt")


