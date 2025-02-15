# For printing something in python we use print function

print("Adnan Shakir")

# Data Types in Python
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# None Type: NoneType

x="Adnan"
print(type(x))     # string

y=123
print(type(y))     # int

a=2.05
print(type(a))     # float

ab=False           # Boolean
print(type(ab))

cd= None           # None
print(type(cd))

b =complex(2j)     # complex
print(type(b)) 

c=["apple","Mango","Pineapple","Banana"]    # list
print(type(c))

d=("Apple","Mango","Banana","Pineapple")    # Tuple
print(type(d))

e=dict(name="Adnan",age=24)                 # Dictionary
print(type(e))

# Variable in Python
# Variable are the container 

x="Adnan"
print(x)

y= 123
print(y)

z="Hello World"
print(z)

# Type Casting

f=str(3)        # integer will become string '3'
print(type(f))

g=int("3")
print(type(g))  # It will return integer 3

h=float("3")    # It will return float 3.0
print(type(h))

# Three Techniques For assigning a variable
# Camel Case 
myNameIs="Adnan"

#Pascal Case
MyNameIs="Adnan"

# Snake Case
my_name_is="Adnan"

# Assigning multiple values to multiple variables
i,j,k='i','love','Pakistan'
print(i,j,k)                # i love Pakistan

l=m=n="Hello"
print(l)        # Hello
print(m)        # Hello
print(n)        # Hello

fruits=["apple","Mango","Banana"]
p,q,r=fruits
print(p)        # apple
print(q)        # Mango
print(r)        # Banana

s="Python"
t="is"
u="awesome"
print(s+t+u)       # Pythonisawesome
print(s,t,u)      # Python is awesome
