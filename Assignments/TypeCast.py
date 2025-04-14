
# 1. Implicit Type Casting
print("\n Implicit Type Casting")
a = 10         # int
b = 5.5        # float
result = a + b # float
print(result)        
print(type(result))      



# 2. Explicit Type Casting
print("\n Explicit Type Casting")
# int()
print("\n int() ")
print(int(5.9))            # 5
print(int("10"))           # 10
print(int(True))           # 1

# float()
print("\n float() ")
print(float(10))           # 10.0
print(float("3.14"))       # 3.14
print(float(False))        # 0.0

# str()
print("\n str() ")
print(str(123))            # "123"
print(str(3.14))           # "3.14"
print(str(True))           # "True"

# bool()
print("\n bool() ")
print(bool(0))             # False
print(bool(1))             # True
print(bool(""))            # False
print(bool("hello"))       # True
print(bool([]))            # False
print(bool([1, 2]))        # True

# complex()
print("\n complex() ")
print(complex(5))          # (5+0j)
print(complex(2, 3))       # (2+3j)
print(complex("4+2j"))     # (4+2j)

# list()
print("\n list() ")
print(list("abc"))         # ['a', 'b', 'c']
print(list((1, 2, 3)))     # [1, 2, 3]
print(list({10, 20}))      # [10, 20] (order may vary)

# tuple()
print("\n tuple() ")
print(tuple("xyz"))        # ('x', 'y', 'z')
print(tuple([1, 2]))       # (1, 2)

# set()
print("\n set() ")
print(set([1, 2, 2, 3]))   # {1, 2, 3}
print(set("banana"))       # {'b', 'a', 'n'} (order may vary)

# dict()
print("\n dict() ")
print(dict([(1, "a"), (2, "b")]))   # {1: 'a', 2: 'b'}
print(dict({3: 'c', 4: 'd'}))       # {3: 'c', 4: 'd'}

# bytes()
print("\n bytes() ")
print(bytes("hello", "utf-8"))     # b'hello'
print(bytes([65, 66, 67]))         # b'ABC'

# bytearray()
print("\n bytearray() ")
print(bytearray("abc", "utf-8"))   # bytearray(b'abc')

# frozenset()
print("\n frozenset() ")
print(frozenset([1, 2, 3, 2]))     # frozenset({1, 2, 3})
