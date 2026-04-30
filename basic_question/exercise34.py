def Reverse_pattern(row):
    for n in range(row, 0, -1):
        for m in  range(0, n):
            print("*", end="")        
        print()



number_of_rows = int(input("Enter the number of rows: "))
Reverse_pattern(number_of_rows)