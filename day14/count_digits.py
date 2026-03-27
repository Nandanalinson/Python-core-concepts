# wap to get the total count of digits in the number

number = int(input("Enter a number : "))

count = 0

while(number > 0):

    last_digit = number % 10 

    count += 1

    number = number // 10

print(f"Count of digits is {count}")



# or


# count = len(str(number))