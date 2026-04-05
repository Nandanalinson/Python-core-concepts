def sum_of(*args):

    sum = 0

    for i in args:

        sum += i

    return sum

n = int(input("Enter how many numbers : "))

numbers = []

for i in range(n):

    num = int(input(f"Enter the number : "))

    numbers.append(num)

print(f"The sum is {sum_of(*numbers)}")