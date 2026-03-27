
"""
to check a number is perfect or not

a positive number that is equal to the sum of its proper positive divisors,
excluding the number itself. for example , 6 is a perfect number bcoz its proper divisors are 1,2, and 3
which when added is equal to 6. another example is 28 , divisiors are 1,2,4,7,14 sum = 28

"""
def perfect(num:int):

    sum = 0

    for i in range(1,num):

        if num % i == 0:

            sum += i

    print("perfect number" if sum == num else "not perfect")

perfect(num = int(input("Enter a number : ")))