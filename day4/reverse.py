number = 453

num1 = number // 100 # 453 // 100 = 4

number = number - (num1 * 100) # 453 - ( 4 * 100 ) = 53

num2 = number // 10 # 53 // 10 = 5

number = number - (num2 * 10) # 53 - ( 5 * 10) = 3

print(( number * 100 )+ (num2 * 10 ) + num1)

#or

print(str(number) + str(num2) + str(num1))