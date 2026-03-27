Amount = int(input("Enter the purchased amount : "))

if Amount >= 1000 :

    Amount -= (Amount/100) * 20
    print(f"The total amount after discount is {Amount}")

else :

    Amount -= (Amount/100) * 5
    print(f"The total amount after discount is {Amount}")
