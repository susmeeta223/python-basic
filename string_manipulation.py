sentence = input("Enter a sentence: ")
vowel = "aeiouAEIOU"
vowel_count = 0

for char in sentence: 
    if char in vowel:
        vowel_count += 1

print(f"The total number of vowel in the sentence is: {vowel_count}")