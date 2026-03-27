number = int(input("Enter a number : "))

product = 1

while(number > 0):

    digit = number % 10

    if digit % 2 == 0:

        product = product * digit

    number = number // 10

print(f"The product of even numbers is {product}")