num1 = [1,2,3,4,5,6,7,8]

num2 = [1,4,8,15,9,10]

new_num = []

for i in num1:

    for j in num2:

        if i == j:

            new_num.append(i)

print(new_num)