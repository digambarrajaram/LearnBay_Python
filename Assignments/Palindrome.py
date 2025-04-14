#1. Palindrome
#Program to check plaindrome string 
print("\n Program to check plaindrome string ")
str1 = 'RADAR'
str2 = ''
i = 1
while i <= len(str1):
    str2 = str2 + str1[len(str1)-i]
    i +=1
    #print(str1 , str2)
if str1 == str2:
    print(' String is palindrome')
else:
    print(' String is not palindrome')