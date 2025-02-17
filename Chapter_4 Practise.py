# 1.Write a program to store seven fruits in a list entered by the user.

fruits=[]

f1=input("Enter the 1st fruit: ")
fruits.append(f1)

f2=input("Enter the 2nd fruit: ")
fruits.append(f2)

f3=input("Enter the 3rd fruit: ")
fruits.append(f3)

f4=input("Enter the 4th fruit: ")
fruits.append(f4)

print("The Entered Fruits are:",fruits)

# 2.Write a program to accept marks Of 6 Students and display them in a sorted
# manner.

Marks=[]
m1=input("Enter the marks of !st Student: ")
Marks.append(m1)

m2=input("Enter the marks of 2nd Student: ")
Marks.append(m2)

m3=input("Enter the marks of 3rd Student: ")
Marks.append(m3)

m4=input("Enter the marks of 4th Student: ")
Marks.append(m4)

m5=input("Enter the marks of 5tH Student: ")
Marks.append(m5)

m6=input("Enter the marks of 6tH Student: ")
Marks.append(m6)

Marks.sort()
print(Marks)

# 3.Check that a tuple type cannot be changed in python.

a=(10,"Adnan",10,45.5,"Ahmed")
a[0]="Ali"

# 4.Write a program to Sum a list with 4 numbers.
list=[1,2,3,4]
print(sum(list))

# 5.Write a program to count the number of zeros in the following tuple:
l2=(0,10,5,8,"Ali","Adnan",0,"Raza",0)
print(l2.count(0))
