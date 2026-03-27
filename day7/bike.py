price = int(input("Enter the price of the bike : "))

if price > 100000:

    tax = (price/100)*10
    print(f"Total price is {price + tax}")

elif (price > 50000) and (price <= 100000):

    tax = (price/100)*7
    print(f"your total price is {price + tax}")

else:

    tax = (price/100)*5
    print(f"your total price is {price + tax}")
