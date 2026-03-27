# sorted() - Return a new list containing all items from the iterable in ascending order.

def is_anagram(word1,word2):

    return True if sorted(word1) == sorted(word2) else False

print(is_anagram("listen","silent"))

print(is_anagram("eat","ate"))












 








