start = int(input("Enter the starting number : "))

stop = int(input("Enter the stoping number : "))

for num in range(start, stop +1):

    factorial = 1

    for i in range(1,num + 1):
    
        factorial *= i
         
    print(f"The factorial of {num} is {factorial}")

