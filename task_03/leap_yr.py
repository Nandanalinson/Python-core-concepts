Year = int(input("Enter the year : "))

if Year % 100 == 0:

    if ((Year % 400 == 0) and ( Year % 4 == 0)):

        print(f"It is a leap year")

    else:

        print(f"it is not a leap year")

elif Year % 4 == 0:

    print(f"it is a leap year")

else:

    print(f"It is not a leap year")