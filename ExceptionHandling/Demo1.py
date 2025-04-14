'''try:
    a = 10
    b = 0

    print("Before Exception")
    result = a/b
    print(result)
except:
    print("Error: The number division by Zero")

try:

    a = 10
    b = 0

    result = a/b
    print(result)

    numbers = [2,3,4,5,6,11]
    print(numbers[9])

except ZeroDivisionError as e :
    print("Error: The number division by Zero ---> ",e)

except IndexError as i :
    print('Index out of range elements not accessible ---> ',i)'''



#Python try with else block 
try:
    num = 1
    assert num%2 == 0

except:         #except block only execute when assert condition will false
    print('not an even number')

else:
    r = 1/num
    print(r)

finally:
    print('Finally block always execute')