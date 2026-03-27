#ngiven the head of a linked list , remove the nth node from the end of the list and return its head.

numbers = [1,4,7,8,3,5,2]

n = int(input("Enter the index position : "))

new_list = []

numbers.pop(-n)

print(numbers)

# val = numbers[-n]

# for i in numbers:

#     if i != val :

#         new_list.append(i)

# print(new_list)