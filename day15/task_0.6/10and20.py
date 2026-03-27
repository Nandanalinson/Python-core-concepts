num = int(input("Enter a number between 10 and 20 :"))

while(num <= 10 or num >= 20):

    if num <= 10 :

        print(f"{num} is too low")

        num = int(input("Try Again , Enter a number : "))

    elif num >= 20 :

        print(f"{num} is too high")

        num = int(input("Try Again , Enter a number : "))

    else:

        exit()

print(f"Thankyou")