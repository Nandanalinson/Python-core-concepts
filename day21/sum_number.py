# prgm to find sum of numbers

def sum_numbers(*args):   # *args is a tuple which can store the all the arguments we give . with this we can call the function multiple times with 

    print(args)           # different no of arguments. args is not the only name we can give , we can also give *nums , *numbers ... etc...* is the imp thing

    sum = 0               # *args is iterable

    for i in args:

        sum += i

    return sum

print(sum_numbers(10,30))       # 40

print(sum_numbers(10,30,40))        # 80


# args* >>> used to pass a variable(different) count of arguments to the function in each call
