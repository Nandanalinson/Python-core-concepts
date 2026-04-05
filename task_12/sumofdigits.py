number = int(input("Enter a number : "))

sum = 0

while(number > 0):

    last_digit = number % 10

    sum = sum + last_digit

    number = number // 10

print(f"The total sum is {sum}")