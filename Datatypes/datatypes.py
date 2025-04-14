
# 1. Numeric Type Datatype
print('1. Numeric Type Datatype :- ')

# 1.1 Interger Datatype
print('1.1 Interger Datatype')
num = 10
print('Int value -> ', num)
print('Function to find which type of datatype it is -> ',type(num))
#print(type(num) ,' Hello', num)
#Predefined Methods in Interger Datatype
print('Predefined Methods in Interger Datatype')
num1 = -2
#num2 = abs(num1)
print('Absolute value ->',abs(num1))
print('Binary value ->',bin(10))  
print('Hexa Decimal Value ->',hex(10))
print('Oct Value ->', oct(10))
print('Powere of Number 2 is ->',pow(3,2))
print('Powere of Number 2 is ->',pow(3,4))
print('Funtion to convert from String to Int -> ',int("123"))     # Convert string to int -> 123
print(divmod(10, 3))  # Quotient and remainder -> (3, 1)


print('\n')
print('----------------------------------------------------------------------------------------------')
#1.2 Float Datatype
print('1.2 Float Datatype')
F1 = 30.3342
print('Float value -> ', F1)
print('Function to find which type of datatype it is -> ',type(F1))
#Predefined Methods in Float Datatype
print('Predefined Methods in Float Datatype')
print('Round of function -> ',round(F1))
print('Round of function to specific position -> ',round(F1,3))
print('Float function to convert number to Float value ->',float(10))
print(F1.is_integer())  # Check if number is integer -> False


print('\n')
print('----------------------------------------------------------------------------------------------')
# 1.3 Complex Datatype
print('1.3 Complex Datatype')
comp = 3 + 4j
print('Complex Datatype -> ',comp)
print('Function to find which type of datatype it is -> ',type(comp))
#Predefined Methods in Complex Datatype
print('Predefined Methods in Complex Datatype')
print('Function to find real part from complex number -> ',comp.real)
print('Function to find imag part from complex number -> ',comp.imag) 

print('\n')
print('----------------------------------------------------------------------------------------------')
# 2. Sequence Type Datatypes 
print('2. Sequence Type Datatypes :- ')

# 2.1 String Datatype 
print('2.1 String Datatype')
str1 = 'hello world'
print('String Datatype -> ',str1)
print('Function to find which type of datatype it is -> ',type(str1))
#Predefined Methods in String Datatype
print('Predefined Methods in String Datatype')
#print('Function to convert from lower case to upper case -> ', str2 := str1.upper(), str3 := str2.lower(), str3)
print('Function to convert from lower case to upper case -> ', str1.upper())
print('Function to convert from upper case to lower case -> ', str1.lower())
print('Function for Title -> ', str1.title())
str2 = 'hello, how are you'
print(str2)
print('Function to replace all occurrences of character -> ', str2.replace('h','H'))
print('Function to replace 1st occurrences of any character -> ', str2.replace('h','H',3)) #Number 1 indicates how many occurrences need to replace
str4 = 'Bye Hello'
print('Funcation to split into a list -> ', str4.split(' '))
print('Function to swapcase word -> ', str4.swapcase()) 
print('Function to Count occurrences of any character -> ', str4.count('y')) 
print('Function to find Index of substring  -> ', str4.find('H')) #Function  tells index of word or character. If not found returns -1.
#print(str4.join(['a','b','c','d']))
print('Function to remove leading/trailing spaces ->',str4.strip())  # Remove leading/trailing spaces
print('Function to check string start with hello ->',str4.startswith("hello"))  # Check if starts with 'hello' -> True
print('Function to check string ends with Hello ->',str4.endswith("Hello"))  # Check if ends with 'Hello' -> True
print('Function to Check if all characters are digits ->',"str4".isdigit())  # Check if all characters are digits -> False
print('Function to check if all characters are alphabets ->',"str4".isalpha())  # Check if all characters are alphabets -> False
print('Function to Check if all characters are lowercase ->',str4.islower())  # Check if all characters are lowercase -> True
print('Function to Check if all characters are uppercase ->',str4.isupper())  # Check if all characters are uppercase -> False


#program to replace any specific character from string
# text = "hello how are you?"
# print(text.split('h', 2))
# parts = text.split('h', 2)  # Split at the second occurrence
# print('h'.join(parts[:1]) + 'H' + 'h'.join(parts[1:]))  


print('\n')
print('----------------------------------------------------------------------------------------------')
# 2.2 List Datatype 
print('2.2 List Datatype')

list1 = [1,3,5,9]   #Initilization of list. list can contain any type of datatype values ex :- list1 = [1,'hello',5,true,9.4]
print('List Datatype -> ',list1)
print('Function to find which type of datatype it is -> ',type(list1))
#Predefined Methods in List Datatype
print('Predefined Methods in List Datatype')
print('Function to append element into list -> ', list1.append(3), list1)
print('Function to insert element into list -> ', list1.insert(2,'A'), list1) #This finction insert value into list by changing current value index to next index
print('Function to reverse element of list -> ',list1.reverse(), list1)
print('Function to Extend list -> ',list1.extend([60.3, 71.2]),list1)  # Extend list
print('Function to remove element from list -> ', list1.remove(3), list1)
print('Function to remove last element from list -> ', list1.pop(), list1)
ex = [7,5,9.3,3,4,3.3,7]
print(ex)
print('Function to sort element of list -> ', ex.sort(), ex) #Only applicable for Int and Float values
print('Function to count occurrences of element -> ', ex.count(7))
print('Function to find index of any element -> ', ex.index(7))


print('\n')
print('----------------------------------------------------------------------------------------------')
# 2.3 Tuple Datatype 
print('2.3 Tuple Datatype')
tup = (1,2,5,2,4)
print('Tuple Datatype -> ',tup)
print('Function to find which type of datatype it is -> ',type(tup))
#Predefined Methods in List Datatype
tuple1 = (10, 20, 30, 40)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (1, "Hello", 3.14, True)
tuple4 = ()  # Empty tuple
tuple5 = (5,)  # Single-element tuple (comma is required)
print(tuple1,tuple2,tuple3,tuple4,tuple5)

print('Accessing Elements in a Tuple -> ', tuple1[0],tuple1[-1])
print(tuple2[1:4])  # Slicing -> (20, 30, 40)
print(tuple3.count(True))  # Count occurrences of 1 -> 3
print(tuple3.index(1))  # Get index of element 3 -> 2

print('\n')
print('----------------------------------------------------------------------------------------------')
# 2.4 Range Datatype 
print('2.4 Range Datatype')
rng = range(2,20,2) #range(start,stop,step)
print(list(rng))


print('\n')
print('----------------------------------------------------------------------------------------------')
# 3. Set Types 
print('3. Set Types :- ')

# 3.1 Set Datatypes
print('3.1 Set Datatype')
set1 = {1,3,2,3}
print('Function to find which type of datatype it is -> ',type(set1))
print('In set duplicate values will be removed automatically -> ',set1) #Set not contain multiple values

print('Adding Elements in set')
s = {1,2,3}
s.add(4)
print('Function to add element in set s.add(4) -> ',s)
s.update([5,6,7])
print('Function to add multiple elements in set s.update([5,6,7]) -> ',s)

print('Removing Elements in set')
s.remove(7)
print('Function to remove element from set s.remove(7) -> ',s) # Removes 7 (raises error if not found)
s.discard(6)
print('Function to discard element from set s.discard(6) -> ',s) # Tries to remove 6 (no error if not found)
s.pop()
print('Function to pop a random element from set s.pop() -> ',s) # Removes a random element
s.clear()
print('Function to clear all elements from set s.clear() -> ',s) # Removes all elements

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))  # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  # {3, 4}
print(set1.difference(set2))  # {1, 2}
print(set1.symmetric_difference(set2))  # {1, 2, 5, 6}

set1.intersection_update(set2)
print(set1)  # Keeps only common elements {3, 4}

set1 = {1, 2, 3, 4}
set1.difference_update(set2)
print(set1)  # Removes elements found in set2 -> {1, 2}

set1 = {1, 2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)  # Keeps only non-common elements {1, 2, 5, 6}

'''a = {1, 2}
b = {1, 2, 3, 4}'''

'''print(a.issubset(b))  # True (a ⊆ b)
print(b.issuperset(a))  # True (b ⊇ a)
print(a.isdisjoint({5, 6}))  # True (no common elements)
'''
list_to_set = [1,1,2,3,4,3]
print('list values -> ',list_to_set)
toSet = set(list_to_set)
print('list values converted to set -> ',toSet)


# 4. Mapping Types 
print('4. Mapping Type :- ')

# 4.1 Dictionary (dict)
print('4.1 Dictionary (dict)')

my_dict = {'Name': 'Dig', 'Age':24}
print('Function to find which type of datatype it is -> ',type(my_dict))
print('Dictionary value -> ', my_dict)

print('Function to print Keys of Dictionary my_dict.keys() -> ',my_dict.keys())
print('Function to print values of Dictionary my_dict.values() -> ',my_dict.values())
print('Function to print items of Dictionary my_dict.items() -> ',my_dict.items())
print("Function to get elements from Dictionary my_dict.get('Name') -> ",my_dict.get('Name'))
print("Function to get elements from Dictionary my_dict.get('add','Not Found') -> ",my_dict.get('add','Not Found'))


my_dict['Age']=26
print("Updating value in Dictionary my_dict['Age']=26 -> ",my_dict)
my_dict['salary']=100000
print("Adding new element in Dictionary my_dict['salary']=100000 -> ",my_dict)

print("Removing value from Dictionary -> ", my_dict.pop('Age') , my_dict)
print("Removing last item from Dictionary -> ", my_dict.popitem(), my_dict)
print("Removes all elements from Dictionary -> ", my_dict.clear() or my_dict)

print("Adds 'city' if not present in Dictionary -> ",my_dict.setdefault('city','Mumbai'))

print('1st Dictionary values -> ',dict1 := {'Name':'Digambar','Age':24})
print('2nd Dictionary Values -> ',dict2 := {'City':'Mumbai','Age':25})
print('Updating 1st Dictionary value with 2nd Dictionary', dict1.update(dict2) or dict1)

# 5. Boolean Types 
print('5. Boolean Type :- ')
status = True
print('Function to find which type of datatype it is -> ',type(status))
print(status)
print(bool(1))
print(bool(0))




