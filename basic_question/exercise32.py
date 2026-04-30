def Square(x):
    dict_square = {}
    for i in range(1, x + 1):
        dict_square[i] = i * i
    return dict_square

x = int(input("Range 1 to "))
print(Square(x))