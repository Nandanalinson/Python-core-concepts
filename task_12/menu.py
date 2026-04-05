n = "y"

while n == "y" or n == "Y":

    ch = int(input("Enter your choice : \n1.ADD \n2.SUBTRACT\n0.EXIT\n"))

    match ch:
        case 0:

            exit()

        case 1:

            num1 = int(input("Enter a number : "))

            num2 = int(input("Enter a number : "))

            print(f"Sum is {num1 + num2}")

        case 2:

            num1 = int(input("Enter a number : "))

            num2 = int(input("Enter a number : "))

            print(f"Difference is {num1 - num2}")

    n = input("Do you want to continue (y/n) : ")
