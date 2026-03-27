units = int(input("Enter the units consumed : "))

if units <= 100 :

    total_bill = units * 5

elif units <= 200 :

    total_bill = (100 * 5) + ((units - 100) * 7)

elif units <= 300 :

    total_bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

else :

    total_bill = (100 * 5) + (100 * 7) + (200 * 10) + ((units - 300) * 15)

print(f"Your total electricity bill is {total_bill}")
