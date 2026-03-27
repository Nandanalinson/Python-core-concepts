numbers = [9,5,2,4,10,55,45]

second_largest = numbers[0]

largest = numbers[0]

for i in numbers:

    if i > largest:   #  10 >  9

        second_largest = largest

        largest = i

    elif i > second_largest and i < largest :

        second_largest = i 


print(second_largest)
