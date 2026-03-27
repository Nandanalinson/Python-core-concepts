# number = int(input("Enter a number : "))

# if number % 5 == 0:

#     print(f"{number} is divisible by 5")

# elif number % 3 == 0:

#     print(f"{number} is divisible by 3")

# else:

#     print(f"Thank you")


number = int(input("Enter a number : "))

if number % 5 == 0:

    if number % 3 == 0:

        print(f"{number} is divisible by both 5 and 3")
    
    else:

        print(f"{number} is divisible by 5 not divisible by 3")

else:

    print(f"{number} is not divisible by 5")