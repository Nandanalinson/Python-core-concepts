# a positive integer where the sum of the factorials of its digits equals the number itself

num = int(input("Enter the number : "))

temp = num

sum = 0

# while(num > 0):

#     digit = num % 10

#     fact = 1

#     for i in range(1, digit + 1):

#         fact *= i

#     sum += fact

#     num = num//10

# print(f"{temp} is strong number" if temp == sum else f"{temp} is not strong number")



for i in str(num):

    for j in range(1 , int(i+1)):
        
        fact *= i
    
    sum += fact
    
    num = num//10
    
print(f"{temp} is strong number" if temp == sum else f"{temp} is not strong number")

