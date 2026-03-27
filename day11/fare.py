distance = int(input("Enter the distance in km : "))

wait_time = int(input("Enter the waiting time in minutes : "))

if wait_time > 5 :

    fare = 50 + distance * 10 + wait_time * 2
    fare = fare/2 if fare > 300 else fare

else :

    fare = 50 + distance * 10
    fare = fare/2 if fare > 300 else fare

print(f"Your total fare is {fare}")


# if wait_time > 5 :

#     fare = 50 + distance * 10 + wait_time * 2

# else :

#     fare = 50 + distance * 10

# if fare > 300 :

#     fare = fare * (50/100)

# print(f"Fare is {fare}")