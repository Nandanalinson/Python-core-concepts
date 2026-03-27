number_1 = int(input("Enter the first number : "))

number_2 = int(input("Enter the second number : "))

number_3 = int(input("Enter the third number : "))


if number_1 > number_2 :

    if number_1 > number_3 :

        print(f"{number_1} is largest")

    else :

        print(f"{number_3} is largest")

else:

    if number_2 > number_3 :
        
        print(f"{number_2} is largest")

    else :

        print(f"{number_3} is largest")
