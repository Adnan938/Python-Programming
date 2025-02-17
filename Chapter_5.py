# Dictionary
s={}        #Empty dictionary

# PROPERTIES OF PYTHON DICTIONARIES
# It is unordered.
# It is mutable.
# It is indexed.
# Cannot contain duplicate keys.

marks = {
    "Adnan":88,
    "Ali":80,
    "Ahmed":66,
    "Raza": 55

}
print(marks,type(marks))
print(marks["Ali"])

# Methods of Dictionary
print(marks.items())    #([('Adnan', 88), ('Ali', 80), ('Ahmed', 66), ('Raza', 55)])
print(marks.keys())     #(['Adnan', 'Ali', 'Ahmed', 'Raza'])
print(marks.values())   #([88, 80, 66, 55])

print(marks.update({"Farhan":99,"Sheraz":75}))    #{'Adnan': 88, 'Ali': 80, 'Ahmed': 66, 'Raza': 55, 'Farhan': 99, 'Sheraz': 75}
print(marks)

print(marks.get("Zain"))        # It shows none ,not error
print(marks.pop("Raza"))        #Raza will be remove
print(marks)

# Set
s={1,5,32,5,5,5,"Adnan","Ahmed","Zain"}    # order is not maintained or duplication is prohibited
print(s)

# PROPERTIES OF SETS
# Sets are unordered Element's order doesn't matter
# Sets are unindexed => Cannotlaccess elements by index
# There is no way to change items in sets.
# Sets cannot contain duplicate values.

# Methods of Sets
print(type(s))
s.add(55)
print(s)
s.remove(1)
print(s)
s.pop()
print(s)

s.discard("Zain")
print(s,"After Discard")

# s.claear()    Empties the set

# Union
s1={10,20,5,9}
s2={1,7,8,5}
s3=s1.union(s2)
print(s3)

# Intersection
s4=s1.intersection(s2)
print(s4)

