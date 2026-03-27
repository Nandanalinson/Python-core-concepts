word1 = input("Enter first word : ")

word2 = input("Enter second word : ")

def is_anagram(word1,word2):

    return True if sorted(word1) == sorted(word2) else False

print(is_anagram(word1,word2))












 








