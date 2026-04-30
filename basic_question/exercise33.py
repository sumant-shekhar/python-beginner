def old_replacer(text, old, new):
    return text.replace(old, new)

text = input("Enter the text: ")
old = input("Enter the old character to be replaced: ")
new = input("Enter the new character: ")
print(old_replacer(text, old , new))