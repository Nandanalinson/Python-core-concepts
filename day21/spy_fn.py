# A spy number is a number in which the sum of its digits equals the product of its digits.

def is_spy(number:int):

    product = 1

    sum = 0

    for i in str(number):

        product *= int(i)

        sum += int(i)

    return True if product == sum else False

print(is_spy(1124))

print(is_spy(4537))