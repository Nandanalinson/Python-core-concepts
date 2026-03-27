a = 0

b = 1

print(a,b,end=" ")

c = a + b

for i in range(1,8):

    print(c,end=" ")

    a = b

    b = c

    c = a + b
