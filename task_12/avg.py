def average(*args):

    sum = 0

    for i in args :

        sum += i

    return sum / len(args)

n = int(input("Enter how many students mark you have to enter : "))

numbers = []

for i in range(n):

    num = int(input(f"Enter mark {i + 1} : "))

    numbers.append(num)

print(f"The average is {average(*numbers)}")