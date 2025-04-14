def display():
    print("Hello, This is first function")
    print("Hello")

display()


#Calculate area of circule with single argument 

def area(r):
    print('Area of circle is = ',3.142*r*r)

area(5)

#Multi Argument Addition of two numbers 

def add(a,b):
    print('Addition of ',a,' and ', b,' = ', a+b)

add(10,20)


#Same function names with different arguments
def add(a,b,c):
    print('Addition of ',a,' , ',b , ' and ', c,' = ', a+b+c)
    return a+b+c

print(add(10,20,30))



#Addition of two number and then square of sum
def sum(a,b):
    return a+b
s = sum(2,2)
print('Sum = ',s)

def square(s):
    return s*s

print('Square = ',square(s))


#Simple intrest 
t=12
r=10
p = 100
def simpleIntrest(p,r,t):
    return (p*r*t)/100

si = simpleIntrest(p, r , t)
print(si + p)




def outerFuc():
    
    name = 'local'
    age = 30


    def innerFuc():
        #nonlocal name
        name = 'Non Local'

        nonlocal age
        age = 24

        print('Inner Function Name = ',name)
        print('Inner Function Age = ',age)

    innerFuc()
    print('Outer Function Value = ',name)
    print('Outer Function Age = ',age)

outerFuc()
