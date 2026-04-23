times = int(input("Range: 1 to "))
symbol = input("which symbol: ")
for y in range(1,times+1):
    for x in range(y):
        print(symbol, end=" ")
    print()