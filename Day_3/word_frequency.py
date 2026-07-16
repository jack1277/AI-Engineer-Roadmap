def word_frequency(sentence):
    frequency = {}
    words = sentence.split()
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency    

sentence = "I love AI and I love Python"
result = word_frequency(sentence)
for word,count in result.items():
    print(f"{word} : {count}")