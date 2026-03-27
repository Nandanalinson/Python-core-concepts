year = int(input("Enter the year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # (2000 % 4 == 0 and 2000 % 100 != 0) or 2000 % 400 == 0
                                                             # (True and False) or True
                                                             # False or True =====> True

    print(f"{year} is a leap year")

else :
    
    print(f"{year} is not a leap year")