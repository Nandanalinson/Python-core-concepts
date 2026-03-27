num = int(input("Enter a first number : "))

num_1 = int(input('Enter the second number : '))

sum = num + num_1

ch = input("Do you want to add another number (y/n)? ")

while(ch == 'y'):

    num_3 = int(input("Enter a number : "))

    ch = input("Do you want to add another number (y/n)? ")

    sum += num_3

print(f"The sum is {sum}")


"""
num = int(input("Enter a first number : "))

num_1 = int(input('Enter the second number : '))

sum = num + num_1

while(True):

    ch = input("do you want to add another number (y/n)? ")

    if ch == "y":
    
        num_3 = int(input("Enter a number : "))

        sum += num_3

    else:
    
        break

print(f"The sum is {sum}")

"""