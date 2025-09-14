# TO count the vowels and consonents in a string 

def count_vowels_consonants(text):   #fun to count vowels and consonants
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
         if char in vowels:
            vowel_count += 1
         else:
            consonant_count += 1
    
    return vowel_count , consonant_count



string = input("Enter a string : ")
vowels , consonants =count_vowels_consonants (string)

print(f"Vowels : {vowels}")
print(f"Consonanta : {consonants}")
