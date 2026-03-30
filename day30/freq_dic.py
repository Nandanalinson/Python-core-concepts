#wap to find the frequency of elements in the list without using builtin function

items = [1,2,3,4,1,2,3,5,6,7,5]

freq = {}

for i in items:

    if i not in freq:       # if dictionary doesnt has the key (i)

        freq[i] = 1         # then add a new key (i) and assign value 1

    else:                   # if that key is already present

        freq[i] += 1        # just increment the value of that by one

print(freq)                 # {1: 2, 2: 2, 3: 2, 4: 1, 5: 2, 6: 1, 7: 1}




