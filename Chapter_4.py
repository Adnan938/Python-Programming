# lists
friends=["Apple","Orange",5,345.05,"Rohan","Ahmed"]
print(friends[0])           # Apple
print(friends[1:5])         # [Orange,5,345.05,Rohan]

# Methods of Lists

friends.append("Adnan")     # It is used to add the value in the last of list
print(friends)

l1=[1,34,56,3,9,20,10]

l1.sort()       # It is used to sort by ascending order
print(l1)

l1.reverse()    # It is used to reverse the order by descending order
print(l1)

l1.insert(2,125)     # It takes index and value to add in the list 
print(l1)

l1.pop(1)      # It takes index of value to removes 
print(l1)

l1.remove(10)  # It removes the value from list 
print(l1)

# Tuples(It is immutable)

a=(1,45,"Adnan","Ahmed",45.5,False,45,45,10)
print(a)

# Methods of Tuples

b=a.count(45)           # It count the nummber of occurence in the tuple
print(b)

c= a.index("Ahmed")     # It gives the index of the item in tuple
print(c)

print("Adnan" in a)     # Keyword in is used to check the attendance

