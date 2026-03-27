# define a function to get the sum of digit in a number entered by user 

def sum_of_digits(number : int):

    sum = 0

    while(number > 0):

        last_digit = number % 10

        sum += last_digit

        number = number // 10

    return sum

print(sum_of_digits(456))


def sum_digits(num : int):
    
    sum = 0

    for i in str(num):

        sum += int(i)

    return sum

print(sum_digits(123))