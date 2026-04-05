N = int(input("Enter the limit : "))

for i in range(1,N):

    count = len(str(i))

    temp = i

    sum = 0

    while(i > 0):

        digit = i % 10

        sum += digit ** count

        i = i // 10

    print(f"{temp} is armstrong" if sum == temp else f"{temp} is not armstrong")