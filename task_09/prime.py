for number in range(1 , 100):

    for i in range(2,number):

        if number % i == 0:
        
            break

    else:

        print(f"{number}")