# functions

() # callable

# built in functions

# exit()   -  to stop the execution at a line
# print()
# input()

# user-defined functions

# advantages of creating a function
# =================================


# Allows you to write the code once and executes it repeatedly by just calling the function name

# syntax 

# def function_name():  ----> function header

#     statements    ---> function body

# function_name()  ---> call the function / function caller


# def greet():

#     name = input("Enter your name : ")

#     print(f"Hii {name} , gud mrng")

# for i in range(1,10):

#     greet()


#To run the function in another file do like this 
# from folder import file_name
# then file.function_name()
# remember here the file where the function is imported (import.py) , 
# it is in the same folder as basics
# here import and functions are in the same folder



# from functions import functions

# functions.greet()







# wap to find the sum of two numbers using function

# def add(a,b):  # parameters

#     return a + b

# a = int(input("Enter first number : "))

# b = int(input("Enter the second number : "))

# result = add(a,b) #arguments

# print(result)

"""
parameters are the variable [laceholders defined in a function's signature , 
while arguments are the actual values passed to those parameters during a 
function call]
"""

def details(name,age,place,course):

    print(f"{name} just completed the {course} course in {place}")

details(age=22,name="nandana",place="kochi",course="django") #keyword arguments


# local variable

# which has been declared inside a function block

# global variable

# variable which has been declared in the module itself (not inisde a function / method block)

name = "nandana"  # global variable

def sq(n):

    square = n ** 2         # local variable 

    print(square)

sq(3)


# return 

def is_square(number : int):

    square = number ** 2

    return square

print(is_square(3))


# return >>> terminates a function execution and passes a specified value back to caller
# if we are using print() inside the function for return the function result value cannot be used in other parts of program.


def numbers():

    for i in range(1,5):

        return i
    
print(numbers())        # will only print 1 , as the value is returned by the function and it terminates. refer point 1.



# prgm to find sum of numbers

def sum_numbers(*args):   # *args is a tuple which can store the all the arguments we give . with this we can call the function multiple times with 

    print(args)           # different no of arguments. args is not the only name we can give , we can also give *nums , *numbers ... etc...* is the imp thing

    sum = 0

    for i in args:

        sum += i

    return sum

print(sum_numbers(10,30))


# args* >>> used to pass a variable(different) count of arguments to the function in each call


# sorted() - Return a new list containing all items from the iterable in ascending order.

def is_anagram(word1,word2):

    return True if sorted(word1) == sorted(word2) else False

print(is_anagram("listen","silent"))

print(is_anagram("hi","hlo"))

#================================================================================================

def factorial(num):

    if num == 1:

        return 1
    
    else :

        return num * factorial(num - 1)
    

print(factorial(5))


#recursive function

#a programming technique where a function calss itself , directly or indirectly

#complexity is less for recursive function compared to loops

#================================================================================================

def details(**kwargs):  # used to get variable count of keyword arguments
                        # while calling the function

    pass

details(name="nandana",age="22",place="thrissur")

#=============================================================================================

result = lambda num:num ** 2

print(result(2))

# lambda function is an anonymous function bcoz it doesn't have any def keyword or function name

# mainly used for one time call (can call multiple times but mainly used as for one time call)

#syntax >>>>> lambda arguments:expression

# lambda can be used for only one expression function , small functions

# no def or function name

# n number of arguments can be given but only one expression need to be there


#==============================================================================================

result = lambda num : "even" if num % 2 == 0 else "odd"

print(result(5))

# using lambda and ternary operator we can write a function in single line

#===============================================================================================