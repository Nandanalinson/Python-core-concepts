num = [20,34,56,78,12,45]

largest = num[0]

for i in num:

    if i > largest:

        second_largest = largest

        largest = i

    elif i > largest and i != largest:

        second_largest = i

print(f"Second largest is {second_largest}")