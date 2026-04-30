def count_words(sentence):
    words = sentence.split()
    print(type(words))  
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

text = input("Enter a sentence: ")
word_counts = count_words(text)
print("Word counts:", word_counts)
