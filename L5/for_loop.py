veggies = ["potato", "tomato", "brinjal", "corn"]
number = [1,2,3,4,5,6,7,8,9,10]
i = 0
new = []
while i < len(number):
    temp = number[i]*number[i]
    new.append(temp)
    i += 1
print(new)

find = int(input("enter number You want to Find in list: "))

for val in new:
    if(val == find):
        print("Found value: ", val)
        break
    else:
        print("finding..")

# for value in number:
#     print(value)

# for value in veggies:
#     print(value)
# else:
#     print("EnD")