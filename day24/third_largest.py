numbers = [8,5,2,3,7,9,1,-1,-7,4,99]

largest = numbers[0]

second_largest = numbers[1]

third_largest = numbers[2]

for i in numbers:

    if i > largest :

        third_largest = second_largest

        second_largest = largest

        largest = i

    elif i > second_largest :

        third_largest = second_largest

        second_largest = largest

        largest = 1

    elif i > third_largest:

        third_largest = i

print(third_largest)