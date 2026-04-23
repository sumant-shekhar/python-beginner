text = str(input("Sentance = "))
vowel = 0
for char in text:
    if char.lower() in 'aeiou':
        vowel += 1
print("total number of vovel Found:",(vowel))