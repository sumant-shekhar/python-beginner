def Capitalize_text(string):
    words = string.split()
    capitalized_words = []
    for char in words:
        capitalized_words.append(char.capitalize())
    result = " ".join(capitalized_words)
    return print(result)


text = input("Enter a string: ")
Capitalize_text(text)