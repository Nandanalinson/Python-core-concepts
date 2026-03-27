# to get odd numbers from 1 to n in a list

n = int(input("Enter the number : "))

print([i for i in range(1,n+1) if i % 2 != 0 if i > 10])

# List comprehension is used to give the code in one line , note that all list comprehension return a list. 
# if we have to give multiple conditions
# we doesn't have to use and operator , just give the condition.