# Strings operations

# length function
name="Adnan Shakir"
length=len(name)
print(length)

# slicing
print(name[0:3])    # Adn
print(name[1])      # d
print(name[-4: -1]) # dna
print(name[1:4])    # dna
print(name[:4])     # is same as [0:4]  Adna
print(name[1:])     # is same as print(name[1:5])   dnan
print(name[1:5])    # dnan

# String Functions
word = "amazing"
print(word[1:6:2])  #mzn

print(name.endswith("nan"))
print(name.startswith("Ad"))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

print(name.replace("Shakir","Bhatti"))
print(name.find("Bhatti"))

abs= "Adnan is a good \"programmer\"\n and \"developer\""
print(abs)