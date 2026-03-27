def sum_recursive(num):

    if num == 1:

        return 1
    
    else:

        return num + sum_recursive(num - 1)
    
print(sum_recursive(7))

print(sum_recursive(3))
