def factorial(num):

    if num == 1:

        return 1
    
    else :

        return num * factorial(num - 1)
    

print(factorial(5))

print(factorial(9))



#recursive function

#a programming technique where a function calss itself , directly or indirectly

#complexity is less for recursive function compared to loops
