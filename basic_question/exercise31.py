def prime_alternative(n):
    prime_list = []

    # Check for prime numbers from 1 to n
    for i in range(1,n+1):
        count = 0
        for j in range(1,i+1):
            if i%j == 0:
                count += 1
        if count == 2:
            prime_list.append(i)

    # Print alternate prime numbers
    print("Alternate Prime numbers are: ",  prime_list[::2])

# Get user input
n= int(input("Enter a number: "))
prime_alternative(n)