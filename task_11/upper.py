def upper_case(word: str):

    temp = ""

    for ch in word:

        if 'a' <= ch <= 'z':

            temp += chr(ord(ch) - 32)

        else:

            temp += ch

            
    return temp

print(upper_case(input("Enter a word : ")))