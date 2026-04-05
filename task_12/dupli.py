nums = [1, 4, 5, 2, 1, 2, 4, 2, 1, 3, 5, 6]

unique_nums = []

for i in nums:

    if i not in unique_nums:
        
        unique_nums.append(i)

print(unique_nums)