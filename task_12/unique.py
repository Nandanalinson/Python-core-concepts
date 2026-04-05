def unique(nums : list):

    unique = []

    for i in nums :

        if i not in unique:

            unique.append(i)

    return unique

print(f"The unique elements are {unique(list(map(int, input('Enter numbers separated by space: ').split())))}")