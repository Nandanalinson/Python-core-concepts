# wap to find the missing number from this sequence of numbers

numbers = [8,4,6,3,1,5]

for i in range(min(numbers) , max(numbers) + 1):

    if i not in numbers :

        print(i)