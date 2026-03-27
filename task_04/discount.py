Amount = int(input("Enter the purchased amount : "))

Member = input("Are you a member ? (y/n) ")

if Amount >= 1000 and Member == "y":

    discount = (Amount/100) * 20
    print(f"The total amount after discount is {Amount - discount}")

else :

    discount = (Amount/100) * 5
    print(f"The total amount after discount is {Amount - discount}")
