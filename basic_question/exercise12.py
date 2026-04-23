def check(num):
    print("list:", num)
    
    first_num = num[0]
    last_num = num[-1]
    
    print(first_num == last_num)

a = [10, 20, 30, 40, 10]
check(a)
b = [75, 65, 35, 75, 30]
check(b)
c = [1, 2, 3, 4, 5, 1]
check(c)