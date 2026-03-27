number = int(input("Enter a number : "))

largest = 0

while(number > 0):

    last_digit = number % 10

    if last_digit > largest :

        largest = last_digit

    number = number // 10

print(f"Largest number is {largest}")