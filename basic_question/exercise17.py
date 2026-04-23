list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

new = []

for x in list1:
    if (x % 2 != 0):
        new.append(x)
for x in list2:
    if (x % 2 == 0):
        new.append(x)
print("list 1 ", list1)
print("List 2 ", list2)
print("new list ",new)