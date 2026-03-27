numbers = list(range(10,51))

primes = []

# for i in range(10,51):

#     numbers.append(i)

for i in numbers:

    for j in range(2,i):

        if i % j == 0:

            break

    else :

        primes.append(i)

print(primes)