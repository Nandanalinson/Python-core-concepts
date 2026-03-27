list_1 = [2, 6, 9, 5, 4, 3, 1]

largest = list_1[0]

second_largest = list_1[0]

for num in list_1:

    if num > largest:

        second_largest = largest 
        
        largest = num

    elif num > second_largest and num != largest:

        second_largest = num

print(f"The second largest is {second_largest}")

