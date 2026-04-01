def sum_of(*args):

    sum = 0

    for i in args:

        sum += i

    return sum

s = sum_of(10,20,30,40,50)

print(f"the sum of numbers is {s}")