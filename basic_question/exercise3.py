name = str(input("Enter the String: "))
i = 0
print("Printing only even index in ", (name))

while i < len(name):
    if (i % 2 == 0):
        print(name[i])
    i += 1


# for char in name:
#     if(char % 2 == 0):
#         print(char)