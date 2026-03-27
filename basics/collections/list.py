# Collections

a = [10,20,30]  # used to keep multiple values in a single variable 

# variable comntain more than one value

# heterogeneous values can be assigned in a collection

# different types : list,set,tuple,dictionary


# LIST
# ========================================================

items = [1,"hello",7.5,True,1]   #iterable

for i in items:

    print(i)


"""
List
=====
# A collection of multiple items stored in single variable . (ordered)
# List is ordered, allow duplicates (reson : index value is assigned for each vallues)
# Heterogenous (can store values in different datatypes)
    eg > items = [1,"hello",9.8,True,1]
# It has zero based indexing similar to string
# It is iterable

# List is Mutable >> Modify >> add a new element , delete a element
# Methods

"""

# LIST METHODS 

items = [1,True,"hello","Data Science",1]

# To add a new element to the end of the list

items.append("python")     #or items.append(object = "python") # add object to the end of list

print(items)

# To insert a element in the specific position

items.insert(0,"java")  # Insert object before index, specify cheyitha index il nammade object insert avum. # ['java', 1, True, 'hello', 'Data Science', 'python']

print(items)

num = [1,2,3,4]

num.insert(-1,10)     #[1,2,3,10,4]         # inserted at the -1 index and then the value is shifted

# To remove a element from the list and get the removed value from the list

value = items.pop(2)   # Remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.

print(value) # True

print(items) # ['java', 1, 'hello', 'Data Science', 1, 'python']

# To remove a value from the list

items.remove(1)  # Remove first occurrence of value.
                 # Raises ValueError if the value is not present.

print(items)     # ['java', 'hello', 'Data Science', 1, 'python'] >>> only first occurance of 1 removed


items.clear()   # clear all the elements and returns empty list

items.index("hello") #Return first index of value.

print(items.count(1))   #Return number of occurrences of value.  # True is taken as 1 and False is taken as 0

#To create a list with numbers

numbers = list(range(10,51))

text = "python is a programming language"

print(text.split())     # ['python', 'is', 'a', 'programming', 'language'] # Return a list of the substrings in the string, using sep as the separator string

# ==========================================================================================================

# MAP FUNCTION 

numbers = [1,2,3,4,5]

print(list(map(lambda x : x ** 2 , numbers)))           # map function apply the function to each element of the list , string or any iterables

# or

# def square(i):
        # return i ** 2

# print(list(square, numbers))

# ======================================================================================================

numbers = [3,5,8,9,1,10,54]

print(list(filter(lambda x : x % 2 != 0 , numbers)))        #[3, 5, 9, 1]

# Filter
#==========
# filter(function,iterable)
#===========================
"""
filter function takes arguments , functions and a collection. And return only the elements 
from iterable for which the function gives True
"""


#if we give map insted of filter then  :

print(list(map(lambda x : x % 2 != 0 , numbers)))           #[True, True, False, True, True, False, False]
#=============================================================================

# REDUCE FUNCTION

#wap to get the sum of numbers in a list


from functools import reduce        # reduce function is not defined globally so we have to import functools

numbers = [1,2,3,4,5,6]

print(reduce(lambda x,y : x + y , numbers))   # Apply a function of two arguments cumulatively to the items of an iterable, from left to right.
                                              # This effectively reduces the iterable to a single value.

                                              
"""
lambda function here it works as
x = 1
y = 2   x + y = 3 , so it goes to x = 3

x = 3
y = 3     so x + y = 6, which is assigned to x , so x = 6

x = 6
y = 4    x + y = 10, so x =10

x = 10
y = 5

so x + y = 15 , x = 15

x = 15
y = 6

so x + y = 21

final answer 21


"""
#===========================================================================================================
# Each user has watched movies (nested list)
# Find the users who watched the same movie more than once

users = [
    ["inception","avatar","inception","hero","hero"],
    ["titanic","avatar"],
    ["joker","joker","joker"]
]

for i in users:

    for movies in i:

        if i.count(movies) > 1 :

            print(i)                    # To print the users history not a single movie

            break


#=============================================================================================================

#LIST COMPREHENSION

# to get odd numbers from 1 to n in a list

n = int(input("Enter the number : "))

print([i for i in range(1,n+1) if i % 2 != 0 if i > 10])

# List comprehension is used to give the code in one line , note that all list comprehension return a list. 
# if we have to give multiple conditions
# we doesn't have to use and operator , just give the condition.

#===========================================================================================================
#TO PASS LIST IN A FUNCTION

def numbers(nums):

    odd = [i for i in nums if i % 2 != 0]

    print(f"The count of odd numbers is {len(odd)}")

    print(f"The avg value of odd numbers is {sum(odd)/len(odd)}")

n = int(input("Enter a number : "))

numbers([i for i in range(1,n+1)])

#============================================================================================================


#STRING IS IMMUTABLE , MEANING IT CANT BE MODIFIED

# Once a string object is created , its value cannot be modified.
# Concatenation behaviour : when you perform s = s + "more" , the original string "s" is not changed.
# Instead a new string is joined with existing one

# Whereas list is mutable we can modifty a list after creating it.

#============================================================================================================

# wap to remove the even numbers from a list
#          i                           so when 2 is removed , i thinks he already checked 0 th position, but 4 moved to the 0 th position 
#          0 1 2 3 4 5 6
numbers = [2,4,6,7,8,9,10]

for i in numbers:

    if i % 2 == 0:

        numbers.remove(i)

print(numbers)

# here we get the output [4,7,9]   its bcoz when we iterate through the list and remove the elements simultanously then the elements change
# to already checked index positions. the problem occurs when there are consecutive even numbers. 


# to slove the issue 

numbers = [2,4,6,7,8,9,10]

for i in numbers.copy():

    if i % 2 == 0:

        numbers.remove(i)

print(numbers)

# now the output is [7,9]. bcoz the iteration happens in the numbers copy , not in numbers. so it doesnt effect when numbers list is modified.