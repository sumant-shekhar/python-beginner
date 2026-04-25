numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
print("Given list:", (numbers))
 
even = []
odd = []
 
for x in numbers:
    if (x % 2 == 0):
        even.append(x)
    else:
        odd.append(x)
 
print("Even numbers:", (even))
print("Odd numbers:", (odd))