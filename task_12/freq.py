nums = [1, 5, 3, 2, 1, 5, 6, 7, 8, 3, 4, 5, 6]

frequency = {}

for i in nums:

    if i in frequency:

        frequency[i] += 1

    else:
        
        frequency[i] = 1

print(frequency)
