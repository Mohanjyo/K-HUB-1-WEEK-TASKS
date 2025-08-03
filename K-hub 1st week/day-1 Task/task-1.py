"""STRINGS AND ITS METHODS: 
strings in python can be denoted by using single quote ('  ') or double quote ("    ")
for example """

print('K-Hub')# --A string inside  single quote 
print("k-Hub")# --A string inside double quote

# Assigning string  to a  variable using single (' ') and double quote(" ")
string  ='K-Hub Task' # using single quote
print(f"-my string:{string}")

my_string ="K-Hub Task" #using double quote
print(f"-my string:{my_string} ")

# assign Multiline string to a variable by using triple single('''  ''') or double quotes(""" """) 
my_intro="""Greetings to everyone, 
myself K.Mohan, pursuing B.tech 3rd year in Kiet group of Institutions of stream Artificial intelligence and Data science"""#using double quote
print(my_intro)

my_intro='''Greetings to everyone, 
myself K.Mohan, pursuing B.tech 3rd year in Kiet group of Institutions of stream Artificial intelligence and Data science'''#using single quote
print(my_intro)

#accessing elements of a string can be done by using square brackets-"[]""
#note from index 0 the string begins and also revese indexing also considered ,a single balnk space also considered as a character including special characters
my_string ="K.Mohan"
print(my_string[0])

#looping through a string
my_string ="K.Mohan"
for x in my_string:
    print(x)
#another example for looping through a string
for x in "K.Mohan":
    print(x)

#To find the length of a string by using a method -"len()"

my_string ="K.Mohan"
print(len(my_string))

# checking a string is present or not ,to check if a certain phrase or character is present in a string we can use keyword " in "

my_string ="accessing elements of a string can be done by using square brackets"
print("string " in my_string)

#another example for checking a string by using condition -" if "

my_string ="accessing elements of a string can be done by using square brackets"
if "string "in my_string:
    print("yes, 'string' is present")

# checking a string if not in

my_string ="accessing elements of a string can be done by using square brackets"
print("mohan" not in my_string)


#STRING METHODS
#Capitalize() - converts the first character to upper case 

my_intro='''Greetings to everyone, 
myself K.Mohan, pursuing B.tech 3rd year in Kiet group of Institutions of stream Artificial intelligence and Data science'''
print(my_intro.capitalize())
mine="36 of age"#when the number is first letter there is no change or use of method capitalize
print(mine.capitalize())

#Casefold() - converts string into lower case
my_intro='''Greetings to everyone, 
myself K.Mohan, pursuing B.tech 3rd year in Kiet group of Institutions of stream Artificial intelligence and Data science'''
print(my_intro.casefold())

# center() - Returns a centered string
#syntax -string.center(length,character)-character is used to fill the empty spaces
my_string ="K.Mohan"
print(my_string.center(143))

#count()- returns the number of times a specified value occurs in a string 
#syntax -string.count(value,start,end)
my_intro='''Greetings to everyone, myself K.Mohan, pursuing B.tech 3rd year in Kiet group of Institutions of stream Artificial intelligence and Data science'''
print(my_intro.count("o"))
print(my_intro.count("o",12,14))

#encode()  -Returns an encoded version of the string
#syntax -string.encode(encoding="encode",errors="errors")
string = "My name is Ståle"
print(string.encode(encoding="ascii",errors="backslashreplace"))#'backslashreplace'	- uses a backslash instead of the character that could not be encoded
print(string.encode(encoding="ascii",errors="ignore"))#'ignore'	- ignores the characters that cannot be encoded
print(string.encode(encoding="ascii",errors="namereplace"))#'namereplace'	- replaces the character with a text explaining the character
print(string.encode(encoding="ascii",errors="replace"))#'strict'	- Default, raises an error on failure
print(string.encode(encoding="ascii",errors="xmlcharrefreplace"))#'xmlcharrefreplace'	- replaces the character with an xml character

#upper()  -Converts a string into upper case
my_string ="K.Mohan"
print(my_string.upper())


#BOOLEAN
"""Booleans represent one of two values: True or False.

Boolean Values
In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False."""

#Print a message based on whether the condition is True or False:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#The bool() function allows you to evaluate any value, and give you True or False in return, 
x = "mohan"
y = 15
print(bool(x))
print(bool(y))


#OPERATORS -Operators are used to perform operations on variables and values.
#There are 7 types of operators in python
"""Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators"""


