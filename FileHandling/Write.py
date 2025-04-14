#Write content into new file
import os

print(os.getcwd()) 
os.chdir("d:\\Python_LB\\FileHandling\\test\\")
print(os.getcwd()) 

text = "Today is tuesday and we are into file handling session"

fp = open('write.txt','w')
fp.write(text)
print("Writing done,Please find content below")
readFile = open('write.txt','r')
data = readFile.read()
print(data)
fp.close()

fp = open('write.txt','r')
print(fp.read())
fp.close()


#reopening the file with append mode 
fp = open('write.txt','a')
fp.write("\nAppending the text into existing file")
print("We have finished writing")
fp.close()



