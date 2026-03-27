# TUPLE 

numbers = ()

numbers = tuple()

# define >>>>>>> () ,tuple()

# zero based indexing . (ordered)

# also called as immutable list

# iterable

# immutable
#===========

# we cannot add or delete any elements from a tuple

# heterogenous : can contain any values 

#ex : numbers = ("hi",1,True,4.5,[],())

# methods are index() and count()

#it allows duplicates

# To add a element to a tuple , convert it into list and then add and then change back to tuple

numbers = ("hi",1,4.5,False)

numbers = list(numbers)

numbers.append("python")

print(tuple(numbers))