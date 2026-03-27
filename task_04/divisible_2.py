number = int(input("Enter a number : "))

if (number % 4 == 0) and (number % 8 != 0):

    print(f"{number} is divisible by 4 but not 8")

else:

    print(f"Either {number} is not divisible by 4 or {number} is divisible by 8")