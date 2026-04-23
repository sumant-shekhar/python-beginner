data = [1, 2, 2, 3, 4, 4, 4, 5]
new = set()
for a in data:
    new.add(a)
new = list(new)
print("Unique List:",(new))
print(type(new))