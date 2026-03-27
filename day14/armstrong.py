#wap to check wheather a number is armstrong or not
#a number is armstrong if the sum of raise to power of no of digits of the number is equal to the same number 
#e.g 153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3   = 3 + 125 + 27 = 153 (here we took raise to 3 bcoz the count of digits in 153 is 3)
#another e.g 54 = 5 ^ 2 + 4 ^ 2 = 25 + 16 = 41 (not a armstrong)
#1634 armstrong


number = int(input("Enter a number : "))

temp = number

count = len(str(number))

sum = 0

while(number > 0):

    last_digit = number % 10

    sum += last_digit ** count

    number = number // 10

print("Armstrong" if temp == sum else "Not Armstrong")
