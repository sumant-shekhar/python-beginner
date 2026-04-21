num = int(input("Number: "))
previous_number = 0
sum = 0
print("printing current and previous number sum in range (",(num),")")

for i in range(num):
    sum = previous_number + i
    print("current Number",(i), "previous Number",(previous_number),"\nSum",(sum))
    previous_number = i