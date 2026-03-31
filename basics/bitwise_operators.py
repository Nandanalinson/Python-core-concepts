# BIT WISE OPERATORS
#===========================

# always works on bits (0 and 1 (integers convert to bits))
# bit by bit operation

# AND (&)
#=======

# compare each bit of two numbers
# 1 & 1 = 1 (results one only if two bits are 1)
# 1 & 0 = 0
# 0 & 1 = 0
# 0 & 0 = 0

print(5 & 3)        # output is 1

print(bin(5)[2:])           # 101           usualy we get as 0b101 so to only get 101 we give[2:]
print(bin(3)[2:])           # 11

"""
1 0 1
0 1 1

========

0 0 1 (& operation, only both 1 we get 1 , otherwise 0)

this is binary 001

so convert it into integer which is 1 

so output 1


1 1 1
1 1 0

======

1 1 0

so integer of 1 1 0 is 6 


"""


# OR (|)
#=======

# compare each bit of two numbers
# 1 | 1 = 1 (results one if any one bit is 1)
# 1 | 0 = 1
# 0 | 1 = 1
# 0 | 0 = 0


print(8 | 5)

"""
1 0 0 0                 # binary of 8
0 1 0 1                 # binary of 5

=========

1 1 0 1

2^3 + 2^2 + 0 + 2^0

8   +  4  + 0 +  1

>>> 13

"""