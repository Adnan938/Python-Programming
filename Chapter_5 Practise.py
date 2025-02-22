# Write a program to create a dictionary ot Hindi words with values as their English
# translation. Provide user with an option to look it up!

Trans={
    "Bhai": "Brother",
    "Behen":"Sister",
    "Sheher":"City",
    "Mulk":"Country"

}
word=input("Enter the word to Translate in English:")
print(Trans[word])

# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

a=set()
a.add(input("Enter the number:"))
a.add(input("Enter the number:"))
a.add(input("Enter the number:"))
a.add(input("Enter the number:"))
a.add(input("Enter the number:"))
a.add(input("Enter the number:"))
a.add(input("Enter the number:"))
a.add(input("Enter the number:"))
print(a,type(a))

# Can we have a set with 18 (int) and "18" (Str) as a value in it?
# What will be the length of following set S:
# s Set ( )
# s.add(20)
# s.add(20.0)

s=set()
s.add(18)
s.add("18")
print(s)                # {'18', 18}

s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)                # {20, '20'} 
print(len(s))           # 2

# What is the type of S?
# s={}
s={}
print(type(s))          # <class 'dict'>

# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

a={}
name=input("Enter the friends name: ")
lang=input("Enter the language: ")
a.update({name:lang})

name=input("Enter the friends name: ")
lang=input("Enter the language: ")
a.update({name:lang})

name=input("Enter the friends name: ")
lang=input("Enter the language: ")
a.update({name:lang})

name=input("Enter the friends name: ")
lang=input("Enter the language: ")
a.update({name:lang})

print(a)        #{'Adnan': 'Python', 'Ali': 'C', 'Fahad': 'C++', 'Faiq': 'C#'}

# If the names of 2 friends are same; what will happen to the program in problem
# 6?
# Answer:The name key will be updated with the second Value

# # If languages of two friends are same; what will happen to the program in problem
# Answer: Nothing will happen the,The values can be same

# Can you change the values inside a list which is contained in set S?
S={8,7,12,[1,2],"Adnan"}

# Answer List can not be stored in a set
