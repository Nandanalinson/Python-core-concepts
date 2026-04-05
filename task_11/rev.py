def rev(word : str):

    temp = ""

    for i in word :

        temp = i + temp

    return temp

print(rev(input("Enter a word : ")))