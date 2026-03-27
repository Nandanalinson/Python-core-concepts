num = 50

num_1 = int(input("Guess the number : "))

count = 0

while(num_1 != num):

    if num_1 < num :

        print(f"{num_1} is too low")

        count += 1
        
        num_1 = int(input("Guess the number : "))


    else:

        print(f"{num_1} is too high")

        count += 1

        num_1 = int(input("Guess the number : "))


print(f"Well done , you took {count} attempts")