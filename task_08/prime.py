for number in range(1,101):

    for i in range(2,number):

        if number % i == 0:

            print(f"{number} is not prime")
        
            break

    else:

        print(f"{number} is prime")