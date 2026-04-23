num = int(input("enter Number:"))
while num > 0:
    d = num % 10
    print(d, end=" ")
    num //= 10