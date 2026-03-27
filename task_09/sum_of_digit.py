n = int(input("Enter a number : "))

def sum_digits(num : int):
    
    sum = 0

    for i in str(num):

        sum += int(i)

    return sum

print(sum_digits(n))