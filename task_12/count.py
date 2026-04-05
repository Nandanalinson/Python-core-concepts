def vowel_count(word : str):

    vowels = "aeiouAEIOU"

    count = 0

    for i in word :

        if i in vowels :

            count += 1

    return count

print(f"The vowel count in the word is {vowel_count(input("Enter a word : "))}")