def sum_sq(num1 : int , num2 : int):

    sum = num1 + num2

    sq = num1 ** 2 , num2 ** 2

    return sum , sq

sum,sq = sum_sq(10,20)

print(f"The sum of numbers is {sum} and square of the numbers is {sq}")