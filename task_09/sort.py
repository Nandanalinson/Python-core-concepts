num = [1,5,8,3,2,9,4]

for i in range(len(num)):

    for j in range(0,len(num) - i - 1):

        if num[j + 1] < num[j]:

            num[j + 1],num[j] = num[j],num[j + 1]

print(num)