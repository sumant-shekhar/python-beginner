dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}
 
print("Dict 1:", (dict1))
print("Dict 2:", (dict2))
 
merged = {}
for key in dict1:
    merged[key] = dict1[key]
for key in dict2:
    merged[key] = dict2[key]
 
print("Merged Dict:", (merged))