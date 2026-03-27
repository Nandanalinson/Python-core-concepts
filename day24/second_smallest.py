numbers = [6,8,33,56,12,99,-1,54,2,1]

smallest = numbers[0]

second_smallest = numbers[1]

for i in numbers:

    if i < smallest :

        second_smallest = smallest

        smallest = i

    elif i < second_smallest and i > smallest:

        second_smallest = i

print(second_smallest)