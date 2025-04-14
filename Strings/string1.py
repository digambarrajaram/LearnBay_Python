str1 = "find index of the string"
#1. Indexing to find Characters
print(str1[1])
print(str1[-1])
print(len(str1))

#2. Slicing :- extracting the small part of the present string as output
print(str1[2:10]) # 2 is starting index and 10 is length of substring or string


#3 .Immutable of string 
"""str1[3] = 'Z'
print(str1)"""

#4. Comparing the strings
s1 = 'Hello Python'
s2 = 'Hello Java'
s3 = 'We are into Learning'
s4 = 'Hello Python'
s5 = 'Hello python'
s6 = 3
s7 = '3'

print(s1==s2)
print(s2==s3)
print(s1==s4)
print(s1==s5)
print(s6==s7)

"""s8 = s6.__str__
print(type(s8))
print(s8==s7)"""

#5. '+' operator = joining of two or more strings
res = s1 + ", "+s3 
print(res)

#6. To find length of the string
print(len(str1))


#7. in / not in ; used in string to check character or word present in string
print('Z' in s1)
print('Python' in s1)


s8 = 'Python is easy to learn and easy to adapt'
print(s8.count('a'))
print(s8.find('to'))

#Program to find 1st and 2nd occurence of character or word in string
s10 = 'Hello, Nice to see you'
KeyValue = 'e'
occToFind = 3
#print(s8[15])
firstIndex = s8.find(KeyValue)
print("First occurence of word=",KeyValue,"index is ",firstIndex)
result = s10.find(KeyValue,s10.find(KeyValue)+(occToFind))
print(occToFind,"occurence of word =",KeyValue,"index is ",result)

#Program to find only 2nd occurence of character or word in string
if occToFind == 1:
    result = s10.find(KeyValue)
else:
    result = s10.find(KeyValue,s10.find(KeyValue)+(occToFind))
print(occToFind,"occurence of word=",KeyValue,"index is ",result)


'''first_value = s8.find('to')
print("Index of First Occurence of to ", first_value)
part = s8.partition('to')
print(part)
sec_value = part[len(part)-1].find('to')
print("Index of Second Occurence of to ", first_value+sec_value)
print(s8[33])

s10 = 'Hello, nice to see you'
value_to_find = 'e'
print(s10[10])
first_value = s10.find(value_to_find)
print("Index of First Occurence of",value_to_find, first_value)
part = s10.partition(value_to_find)
print(part)
sec_value = part[len(part)-1].find(value_to_find)
print("Index of Second Occurence of ",value_to_find, first_value+sec_value)'''



#print(s8[33])
#print(s10.find('e',2))




#8. find :- to find substring from a string
str2 = 'Learn Python'
i = str2.find('Python') # Capital P : Returns index value
print(i)
i = str2.find('python') # Small P : output is -1 if word is not present
print(i)



#9. capitilize : first character of word or sentence will be made as capital
str_cap = 'hello Everyone'
print(str_cap.capitalize())

#10. endwith() mentod
print(str_cap.endswith('ne'))
print(str_cap.endswith('E'))

f = 'Pic.jpg'
if f.endswith(('.jpg','.png')):
    print('File is matched ')
else:
    print('File not matched')


#11,12 .  lowering / upper the case of the string 
print(f.islower())
print(f.isupper())
print(f.lower())
print(f.upper())


#13. replace() :- used to replace substring from parent string and it is applicable for character and words
#s9 = 'python is easy, Python is open source and beginners can learn Python fast Python Python Python Python Python'
s9 = 'Python is easy, Python is open source and beginners can learn Python fast'
print(s9.replace('Python','Java'))
print(s9.replace('Python','Java',1))
print(s9.replace('Python','Java',5)) # 5 indicates number of occurence of any word 



#14.  partition() : it will 
str_prt = 'Python python is Learning'
prt_res = str_prt.partition("for")
prt_res1 = str_prt.partition("is")
print(prt_res)
print(prt_res1)

str_pat2 = "Key : Value"
str_prt3 = str_pat2.partition(':')
print(str_prt3)

s10 = 'Hello, Nice to see you'
KeyValue = 'e'
occToFind = 3
i=0
result = 0
index = 0
occ = 0
for i in range(i,len(s10)):
    if s10[i]==KeyValue:
        occ +=1
        result = s10[i]
        index = '  ' + str(i)
        print(result,'Index of',occ, index)
   

#Program to find any occurence of character in string
print('----------------------------------------')
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
                print(f"Key value '{KeyValue}' {occToFind} occurence index value is {index}")

    

#15. rfind(substring, start,end): tom find highest index of any string
s11 = "Hello, How are you python     "
print(s11.rfind('e'))

#16. rstrip(chars) : remove rxtra trailing spaces from end of the string
print("Length of string before rstrip",len(s11))
print(str12 := s11.rstrip()," : Length of string after rstrip" ,len(str12))


#17. split() : split string into multiple sub strings
str13 = 'Python is easy, Python is open source ,beginners can learn Python fast'
print(str13.split(',')) # ['Python is easy', ' Python is open source ', 'beginners can learn Python fast']
print(str13.split(',',1)) # ['Python is easy', ' Python is open source ,beginners can learn Python fast']
print(str13.split('is',1)) # ['Python ', ' easy, Python is open source ,beginners can learn Python fast']
print(str13.split('is',2)) # ['Python ', ' easy, Python ', ' open source ,beginners can learn Python fast']


#18. swapcase() : Upper case to lower and vice versa
print(str13.swapcase()) #pYTHON IS EASY, pYTHON IS OPEN SOURCE ,BEGINNERS CAN LEARN pYTHON FAST

#19. title() : Convert first char of every word of string into upper case and rest char's will be lower case
print(str13.title()) #Python Is Easy, Python Is Open Source ,Beginners Can Learn Python Fast


#20. removesuffix() : last word 
str14 = 'PythonIs, open source and we use in VisualStudio'
print(str14.removesuffix("Studio")) #PythonIs, open source and we use in Visual

#21. removeprefix() : First word
print(str14.removeprefix("Python")) #Is, open source and we use in VisualStudio








