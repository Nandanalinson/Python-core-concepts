# wap to remove the even numbers from a list 

numbers = [2,4,6,7,8,9,10]

for i in numbers:

    if i % 2 == 0:

        numbers.remove(i)

print(numbers)