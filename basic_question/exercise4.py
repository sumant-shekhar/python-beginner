name = str(input("Enter the String: "))
n = int(input("enter index number: "))

print("last index is",(len(name) - 1))

result = name[n:]
print(result)