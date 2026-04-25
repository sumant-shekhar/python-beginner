list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
 
print("List A:", (list_a))
print("List B:", (list_b))
 
set_a = set(list_a)
set_b = set(list_b)
 
common = set_a & set_b
print("Common Elements:", (common))