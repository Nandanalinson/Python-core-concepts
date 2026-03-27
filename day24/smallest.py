numbers = [2,9,5,4,1,66,32,99,145]

smallest = numbers[0]

for i in numbers:

    if i < smallest:

        smallest = i

print(f"The smallest element is {smallest}")