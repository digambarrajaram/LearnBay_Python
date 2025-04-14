#2. Count of words or characters in string
print("\n Count of words or characters in string")
str1 = 'Python is easy to learn and easy to adapt'
print(" Occurence of 'a' in the string is ",str1.count('a'))


#3. Program to find 1st and 2nd occurence of character or word in string
print("\n Program to find 1st and 2nd occurence of character or word in string")
s10 = 'Hello, Nice to see you'
KeyValue = 'e'
occToFind = 2
#print(s8[15])
firstIndex = s10.find(KeyValue)
print(" First occurence of word=",KeyValue,"index is ",firstIndex)
result = s10.find(KeyValue,s10.find(KeyValue)+(occToFind))
print(occToFind," occurence of word =",KeyValue,"index is ",result)



#3. Program to find any occurence of character in string
print('\n Program to find any occurence of character in string')
s10 = 'Hello, Nice to see you'
KeyValue = 'e'
occToFind = 2
result,index,occ = 0,0,0

if occToFind <= 0:
    print("Invalid occurence value to find ")
elif KeyValue not in s10:
    print('Invalid Key Value')
else:
    for i in range(0,len(s10)):
        if s10[i]==KeyValue:
            occ +=1
            if occ == occToFind:
                result = s10[i]
                index = i
                print(f" Key value '{KeyValue}'s {occToFind} occurence index value is {index}")
