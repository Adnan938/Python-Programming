# Conditional Formating
# if else Statement

age=int(input("Enter Your Age: "))

if(age>18):
    print("You are above the age of consent")
    print("Good For You")

else:
    print("You are below the age of consent")

print("End of Program")

# if elif else statement

age=int(input("Enter Your Age: "))
if(age>18):
    print("You are above the age of consent")
    print("Good For You")

elif(age<0):
    print("Enter the valid age,The age cannot be in negative ")

elif(age==0):
    print("Enter the valid age,The age cannot 0")

else:
    print("You are below the age of consent")

print("End of Program")


# Quiz
a=int(input("Enter your age: "))
if(a>=18):
    print("Yes")

else:
    print("No")

# RELATIONAL OPERATORS
# Relational Operators are used to evaluqte conditions inside the if statements. Some
# examples ot relational operators are:
# == equals,
# >= : greater than/ equal to.
# <= : lesser than/ equal to.

# LOGICAL OPERATORS
# In python logical operators operate on conditional statements. Example:
# and — true if both operands are true else false.
# or — true if at least one operand is true or else false.
# not — inverts true to false & false to true.

num=int(input("Enter the number: "))
if(num%2==0):
    print("The Given number is Even")
else:
    print("The given number is Odd")