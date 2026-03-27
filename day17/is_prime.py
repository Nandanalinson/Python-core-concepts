#ctrl + alt + pg dn / pg up


#identify prime number in a range of numbers

# number = int(input("Enter a number : "))

# for i in range(2,number):

#     if number % i == 0:

#         print(f"{number} is not prime")

#         break
# else :

#     print(f"{number} is prime")



# number = int(input("Enter a number : "))

# if number > 1:

#     for i in range(2,number):

#         print(f"{number} is not prime")

#         break

#     else:

#         print(f"{number} is prime")

# else :

#     print("please enter a number greater than 1")



number = int(input("Enter a number : "))

while(number <= 1):

    print("please enter a number greater than 1")

    number = int(input("Enter a number : "))

for i in range(2,number):

    print(f"{number} is not prime")

    break

else:

    print(f"{number} is prime")







































# number = int(input("Enter a number : "))

# flag = 0

# for i in range(2,number):

#     if number % i == 0:

#         flag = 1

# print(f"{number} is prime" if flag == 0 else f"{number} is not prime")



