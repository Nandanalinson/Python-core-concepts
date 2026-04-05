def calculator(num1 : int,num2 : int):

    ch = int(input("Enter your choice : \n1.ADD\n2.SUBTRACT\n3.DIVIDE\n4.MULTIPLY\n0.EXIT\n"))

    match ch :

        case 0:
            exit()

        case 1: 
            return f"sum is {num1 + num2}"

        case 2:
            return f"Difference is {num1 - num2}"

        case 3:
            return f"Quotient is {num1 / num2}"

        case 4:
            return f"Product is {num1 * num2}"

print(calculator(int(input("Enter a number : ")),int(input("Enter a number : "))))