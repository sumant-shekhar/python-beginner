def pal(number):
    print("Original Number ", number)
    str_number = str(number)
    if str_number == str_number[::-1]:
        print("Yes",(number)," is palindrome number")
    else:
        print("No",(number),"is not a palindrome number")

n = int(input("Enter Number: "))

pal(n)
