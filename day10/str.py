language = "Javascript" #colleection of characters
#           0123456789

"""
a number that indicates the position of a character on a string
python str follows zero based index
index positioning helps the string remains ordered
allows duplicate elements because each element has different position values
used to get a substring from a string
negative indexing starts from -1
"""


# print(language[2]) #v

# print(language[2:8]) #vascri slicing <<<<<< always give one index position more to get the last value , here i need from 2 to 7 , so i gave 2:8

# # slicing : uses indexes to extract specific positions from a string


# print(language[-1]) #to print the last element

# print(language[0::]) #to print from 0 to last element
# print(language[0:]) #to print from 0 to last element

# print(language[3:]) #it print from 3 till the last element

# print(language[:5])

# name = "hello world"

# print(name[2:7]) # "llo w"
# print(name[6]) #"w"
# print(name[5:]) # " world"

# print("Disney" + name[5:]) # "Disney world"

# print(name[0:5] + "Disney" + name[5:]) # "helloDisney world"

# print(name[::-1]) #dlrow olleh #to print in reverse


#=======================================================================================
# methods in string

# name = "Javascript"
# print(name.upper()) #return a copy of the string converted to uppercase.
# print(name.lower()) #Return a copy of the string converted to lowercase.
# print(name.capitalize()) #make the first character have upper case and the rest lowercase.
# print(name.swapcase()) #if input = JavaScript , output will be jAVAsCRIPT
# print(name.count("a")) #count the no of occurances of a substring #2
# print(name.find("v")) #Return the lowest index in S where substring sub is found.
# print(name.index("a")) #Return the lowest index in S where substring sub is found

#========================================================================================

name = " nandana "

print(name.isupper()) #Return True if the string is an uppercase string, False otherwise.
print(name.islower()) #Return True if the string is a lowercase string, False otherwise.
print(name.isalpha()) #Return True if the string is an alphabetic string, False otherwise.
print(name.isalnum()) #Return True if the string is an alpha-numeric string, False otherwise.

print(name.strip()) #Return True if the string is an uppercase string, False otherwise. can't take alphabets only special characters and whitespaces.
print(name.rstrip()) #Return a copy of the string with trailing whitespace removed.
print(name.lstrip()) #Return a copy of the string with leading whitespace removed.

#=========================================================================================