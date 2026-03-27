# wap to get a list of numbers from 1 to 50

numbers = []

for i in range(1,51):

    numbers.append(i)

print(numbers)

# wap to get a list of odd numbers from 1 to 99

odd_nums = []

for i in range(1,100):

    if i % 2 != 0:

        odd_nums.append(i)

print(odd_nums)

# wap to get a list of numbers divisible by 3 and 5 from 100 to 500

num = []

for i in range(100,501):

    if i % 3 == 0 and i % 5 == 0:

        num.append(i)

print(num)

# wap to get a list of odd numbers not divisible by 5 from 1 to 80

nums = []

for i in range(1,81):

    if i % 2 != 0 and i % 5 != 0 :

        nums.append(i)

print(nums)