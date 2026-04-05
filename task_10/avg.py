def average(*args):

    sum = 0

    for i in args:

        sum += i

    return sum / len(args)

n = int(input("How many arguments you want to give : "))

numbers = []

for i in range(n):

    num = int(input("Enter the number : "))
    
    numbers.append(num)

print("Average:", average(*numbers))