#wap to get the sum of numbers in a list

from functools import reduce         # reduce function is not defined globally so we have to import functools

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