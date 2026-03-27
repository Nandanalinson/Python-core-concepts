#identify prime number in a range of numbers

start = int(input("Enter the starting number : "))

stop = int(input("Enter the stoping number : "))

for number in range(start , stop + 1):

    for i in range(2,number):

        if number % i == 0:

            print(f"{number} is not prime")
        
            break

    else:

        print(f"{number} is prime")