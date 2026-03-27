numbers = [3,5,8,9,1,10,54]

print(list(filter(lambda x : x % 2 != 0 , numbers)))        #[3, 5, 9, 1]

# Filter
#==========
# filter(function,iterable)
#===========================
"""
filter function takes arguments , functions and a collection. And return only the elements 
from iterable for which the function gives True
"""