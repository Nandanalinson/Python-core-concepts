def largest(num1 , num2 , num3):

    if num1 > num2 and num1 > num3:

        print(f"The largest number is {num1}")

    elif num2 > num1 and num2 > num3:

        print(f"The largest number is {num2}")

    else:

        print(f"The largest number is {num3}")

largest(int(input("Enter a number : ")),int(input("ENter a number : ")),int(input("Enter a number : ")))
