N = int(input("Enter the limit : "))

a = 0 

b = 1

c = a + b

print(a)

print(b)

while(c <= N):

    print(c)

    a = b

    b = c
    
    c = a + b
