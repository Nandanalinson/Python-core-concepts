n = int(input("Enter the limit : "))

a = 0

b = 1

print(a,b,end=" ")

c = a + b

for i in range(1,n):

    print(c,end=" ")

    a = b

    b = c

    c = a + b
