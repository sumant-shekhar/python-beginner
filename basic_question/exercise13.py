num_list = [10, 20, 33, 46, 55]
print("Given list is", num_list)
print("Divisible by 5:")
new = []
for x in num_list:
    if (x % 5 == 0):
        new.append(x)
print(new)