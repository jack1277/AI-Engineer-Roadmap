def count_vowels(Text):
    count = 0
    for char in Text:
        if char in 'aeiouAEIOU':
            count += 1
    return count

Text = input("Enter a string: ")
vowel_count = count_vowels(Text)
print("Number of vowels:", vowel_count)