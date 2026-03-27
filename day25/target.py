"""
Given a sorted array of distinct integers and a target value , return the index if the target is found.
if not , return the index where it would be if it were inserted in order

numbers = [1,3,5,6]
Enter the target value : 2
The index value of the target if it were in the list is 1


numbers = [1,3,5,6]
Enter the target value : 5
The index of the target in list is 2

"""

numbers = [1,3,5,6]

target = int(input("Enter the target value : "))

if target in numbers :

    print(f"The index of the target in list is {numbers.index(target)}")

elif target not in numbers :

    numbers.append(target)

    numbers.sort()

    print(f"The index value of the target if it were in the list is {numbers.index(target)}")