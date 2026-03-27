# need to ask enter a number and check it is prime or not , it has to asl three times


def is_prime(num:int):

    for i in range(2, num):

        if num % i == 0:

            print(f"{num} is not prime")

            break
    
    else:

        print(f"{num} is prime")

for i in range(3):

    is_prime(num = int(input("Enter a number : ")))