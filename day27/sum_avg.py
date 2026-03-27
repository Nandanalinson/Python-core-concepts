# DEFINE A function which accepts a list of numbers from 1 to n
# then check and return the count and avg of odd numbers in it


def numbers(nums):

    odd = [i for i in nums if i % 2 != 0]

    print(f"The count of odd numbers is {len(odd)}")

    print(f"The avg value of odd numbers is {sum(odd)/len(odd)}")

n = int(input("Enter a number : "))

numbers([i for i in range(1,n+1)])