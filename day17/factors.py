num = int(input("Enter the number : "))

for i in range(1,num+1):

    if num % i == 0:

        print(f"{i} is a factor of {num}")
    
    else:

        print(f"{i} is not a factor of {num}")
