print('--------------------')
age = 18
if age >= 18:
    print("You are eligible for voting")

print('--------------------')
num=10
if num % 2 == 0:
    print("Even")
else:
    print('Odd')

print('--------------------')
marks = 87
if marks >= 90:
    print('grade A')
elif marks >= 80:
    print('Grade B')
elif marks >= 70:
    print('Grade C')

print('--------------------')
x = 10
if x > 5:
    print("x is greater than 5")
    if x > 8:
        print("x is also greater than 8")

print('--------------------')
age = 18 
std = "Adult" if age >= 18 else "minor"
print(std)


print('--------------------')
a = 10
b = 5

if a > 5 and b < 10:
    print("Both conditions are True")

if a > 5 or b > 10:
    print("At least one condition is True")

if not (b > 10):
    print("b is NOT greater than 10")

print('--------------------')

day = 'monday'

match day:
    case "monday":
        print("It's monday")
    case "tuesday":
        print("It's tuesday")
    case _:
        print("It's just another day!")


rain = True
print("It's raining") if rain else print('Enjoy the sunshine!')

flag = [True , False, True]

if all(flag):
    print('All True')
elif any(flag):
    print("At least one value is True")
else:
    print(" All false")