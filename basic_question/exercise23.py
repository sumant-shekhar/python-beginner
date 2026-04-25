num = int(input("Enter Number: "))
original = num
reverse = 0

while num > 0:
    d = num % 10
    reverse = reverse * 10 + d
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")