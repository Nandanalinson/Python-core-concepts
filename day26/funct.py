"""
generate a list with 10 numbers (using range function)

filter the list with values above 10 and even and get the result

find the square of the filtered list of elements

find the sum of squared elements

display all list
"""

# from functools import reduce

# num = list(range(5,16))

# print(f"The generated list is : {num}")

# nums = list(filter(lambda x : x > 10 and x % 2 == 0 , num))

# print(f"Filtered list is {nums}")

# numbers = list(map(lambda x : x ** 2 , nums))

# print(f"The squared list is {numbers}")

# print(f"The sum of elements is {reduce(lambda x,y : x + y,numbers)}")



from functools import reduce

num = list(range(5,16))


nums = list(filter(lambda x : x > 10 and x % 2 == 0 , num))


numbers = list(map(lambda x : x ** 2 , nums))


print(num)

print(nums)

print(numbers)

print(f"The sum of elements is {reduce(lambda x,y : x + y,numbers)}")