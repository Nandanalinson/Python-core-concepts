number = int(input("Enter a number : "))

temp = number

count = len(str(number))

sum = 0

while(number > 0):

    last_digit = number % 10

    sum += last_digit ** count

    number = number // 10

print("Armstrong" if temp == sum else "Not Armstrong")
