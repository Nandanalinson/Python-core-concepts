word = input("Enter a word : ")

vowels = "aeiouAEIOU"

c_count = 0

v_count = 0

d_count = 0

s_count = 0

for i in word :

    if i in vowels:

        v_count += 1

    elif i not in vowels and i.isalpha():       #or i.isalpha()

        c_count += 1

    elif i.isdigit():

        d_count += 1

    else:

        s_count += 1


print(f"The no of vowels is {v_count}, consonants count is {c_count}, digit count is {d_count} , special character count is {s_count}")



# Enter a word : nandana@123
# The no of vowels is 3, consonants count is 4, digit count is 3 , special character count is 1