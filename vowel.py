def checkVowel(word):
    withVowel = [i for i in word if i in ['a','e','i','o','u']]
    return len(withVowel) 


word = input('Input word: ').lower()
print(f"There are {checkVowel(word)} vowels in the {word}")
