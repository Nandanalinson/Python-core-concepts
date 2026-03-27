number = int(input("Enter a number :"))

if (number % 2 == 0) or (number % 7 == 0):

    print(f"{number} is divisible by either 2 or 7")

else:

    print(f"{number} is not divisible by both")