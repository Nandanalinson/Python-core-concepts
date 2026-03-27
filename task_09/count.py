word = input("Enter a word : ")

vowels = "aeiouAEIOU"

c_count = 0

v_count = 0

for i in word :

    if i in vowels:

        v_count += 1

    else:       

        c_count += 1

print(f"The no. of vowels is {v_count} and consonants is {c_count}")