fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("we already have = ",(fruits))
new = fruits.append(input("enter New Fruit: "))
print(fruits)
print("total length of index ", len(fruits)-1)
index = int(input("enter which index(starts with 0) you want to remove: "))
fruits.remove(fruits[index])
print(fruits)