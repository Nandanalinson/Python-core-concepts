number = int(input("Enter a number :"))

if (number % 3 == 0) and (number % 5 == 0):

    print(f"{number} is divisible by both 5 and 3")

elif (number % 3 == 0) or (number % 5 ==0):

    print(f"{number} is divisible by either 3 or 5")

else:

    print(f"{number} is not divisible by both")