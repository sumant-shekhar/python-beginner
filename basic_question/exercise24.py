terms = 15
a = 0
b = 1
print("Fibonacci series upto", terms, "terms:")
 
for i in range(terms):
    print(a, end=" ")
    a , b = b , a + b