# I. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.

name=input("Enter Your Name:")
print("Good Afternoon:",name)
print(f"Good Afternoon:,{name}")

# 2. Write a program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>","Adnan").replace("<|Date|>","15-Jan"))

# Replace the double space from problem 3 with single spaces.
ab = "Adnan is  a good Developer"
print(ab)
print(ab.find("  "))
print(ab.replace("  "," "))

# Write a program to format the following letter using escape sequence
# characters.
# "Dear Harry, this python course is nice. Thanks!
Letters = "Dear Harry, \n \t This python course is nice. \n Thanks! "
print(Letters)