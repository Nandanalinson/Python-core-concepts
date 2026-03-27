# Given a string s consisting of words and spaces , return the length of the last word in the string

text = "python is a programming language"

words = text.split()

print(len(words[-1]))