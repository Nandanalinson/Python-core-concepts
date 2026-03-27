items = [1,"hello",7.5,True,1]   #iterable

for i in items:

    print(i)


"""
List
=====
# A collection of multiple items stored in single variable
# List is ordered, allow duplicates (reson : index value is assigned for each vallues)
# Heterogenous (can store values in different datatypes)
    eg > items = [1,"hello",9.8,True,1]
# It has zero based indexing similar to string
# It is iterable

# List is Mutable >> Modify >> add a new element , delete a element
# Methods

"""


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

