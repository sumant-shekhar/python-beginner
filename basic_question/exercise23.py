def palinedrome(num):
    str_num = str(num)
    rev = str_num[::-1]
    print(num == rev)
    return


x = int(input("x = "))
palinedrome(x)