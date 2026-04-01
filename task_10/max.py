def maximum(*args):

    max = 0

    for i in args:

        if i > max:

            max = i
    
    return max

m = maximum(90,40,50,100)

print(f"The maximum value is {m}")