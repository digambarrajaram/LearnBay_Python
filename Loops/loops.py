
print('For Loop')
for i in range(5):
    print(i)
print('--------------------')
for i in range(10,20):
    print(i)
print('--------------------')
fruits = ['Apple','orange','cherry']
for f in fruits:
    if f == 'orange':
        continue
    print(f)
print('--------------------')
fruits = ['Apple','orange','cherry']
for f in fruits:
    if f == 'orange':
        break
    print(f)

print('--------------------')
str1 = "Hello"
for s in str1:
    print(s)

print('--------------------')
for i in range(0,20,5):
    print(i)

print('--------------------')
for i in range(20,0,-5):
    print(i)

print('--------------------')
student = {"name": "John", "age": 20, "grade": "A"}
for key,values in student.items():
    print(key, ":",values)

print('--------------------')
names = ["Alice", "Bob", "Charlie"]
for index,name in enumerate(names):
    print(index, " -> ", name )

print('--------------------')
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end="\t")
    print()


# While statement
print('while statement')
i = 0
while i<= 5:
    print(i)
    i +=1

#Sum of 1 to 10 numbers 
total = 0
num = 1
while num <= 10:
    total = total + num
    num = num +1
print('Total = ', total)

#Sum of 1 to 10 numbers till sum reaches to 10
total = 0
num = 1
while total < 10:
    total += num
    num += 1
print('Total = ', total)



#Fibonacci Series

Fib = 0
pre,next = 0,1
print(pre,next,end=' ')
while Fib <= 100:
    Fib=pre+next
    pre = next
    next = Fib
    print(Fib, end=' ')



a , b = 6, 10
a , b=b , a+b  # right side = b , a+b ------- 6 , 6 + 10 = 6 ,16;    a,b = 6,16
print(a,b)



limit = 100
a, b = 0,1
while a <= limit:
    print(a, end=' ')
    a , b = b , a+b

s= 'learnbay'
res = ''
print('\n')
for i in s:
    if i == 'e' or i == 'a':
        continue
    print(i, end=' ')
    res = res + i
    """else:
        print(i, end=' ')
    res = res + i"""

print(res)



#Program to remove specific characters from string either Capital or Small 
s= 'lEarnbay'
print('\n')

for i in s:
    if i.lower() == 'e' or i == 'a':
        continue
    print(i,end='')
    #print(i.islower)

str_stm = "Learnbay is coaching"
vowels = 'aeiouAEIOU'
res = ''
index = 0

print(len(str_stm))
while index < len(str_stm):
    if str_stm[index] not in vowels:
       res += str_stm[index]
    index +=1
    
print(res)


print('List Example')
str_list = ['L','e','a','r','n','A']

for i in str_list:
    if i == 'e' or i.lower() == 'a':
        continue
    print(i)


print('Tuple Example')
str_Tuple = ('L','e','a','r','n','A')
for i in str_list:
    if i == 'e' or i.lower() == 'a':
        continue
    print(i)
    
#int_tuple = (10,20,10)
#print(int_tuple.index(20))
v = 'aeiouAEIOU'
index=0
#print(len(str_list))
print('-----------------------')
#print(str_list)
while index < len(str_list):
    if str_list[index] not in v:
        print(str_list[index])
    index += 1

    

a = 90
b = 300
print('a =',a , ' b =',b)
a = a+b
#print(a)
b = a-b
#print(b)
a = a-b
#print(a)
print('a =',a , ' b =',b)



#Program to check plaindrome string 
str1 = 'RADAR'
str2 = ''
iterable = 1
length = len(str1)
for i in str1:
    str2 = str2 + str1[length-iterable]
    iterable +=1
    #print(str1 , str2)
if str1 == str2:
    print('String is palindrome')
else:
    print('String is not palindrome')



#Program to check plaindrome string 
str1 = 'RADAR'
str2 = ''
i = 1
while i <= len(str1):
    str2 = str2 + str1[len(str1)-i]
    i +=1
    #print(str1 , str2)
if str1 == str2:
    print('String is palindrome')
else:
    print('String is not palindrome')