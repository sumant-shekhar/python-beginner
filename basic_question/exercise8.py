char = str(input("enter word: "))
print("text:",(char))
reverse = ""
for a in char:
    reverse = a + reverse
print("reverse:",(reverse))