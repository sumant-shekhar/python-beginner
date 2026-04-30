def Detection(Strings):
    contains_digit = False
    for char in Strings:
        if char.isdigit():
            contains_digit = True
            print(f"The string '{Strings}' contains digits: {contains_digit}")
            break

test = str(input("Enter a string: "))
Detection(test)