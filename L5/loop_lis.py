num = (1,4,9,16,25,36,49,64,81,100)
idx = 0
print(type(num))
x = int(input("which number you want to find in Index: "))
while idx < len(num):
    if(num[idx] == x):
        print("Found at index: ", idx)
        break
    else:
        print("Finding....")
    idx += 1