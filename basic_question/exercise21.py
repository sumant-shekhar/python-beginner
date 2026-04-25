times = int(input("Range: 1 to "))
symbol = input("which symbol: ")
for y in range(times,0,-1):
    while y > 0:
        print(symbol, end=" ")
        y -= 1
    print()