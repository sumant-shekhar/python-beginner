def exponent(base, exp):
    times = exp
    res = 1
    while times > 0:
        res = res * base
        times -= 1
    print((base),"raises to the power of",(exp),"is:",(res))
    return res

base_val = int(input("Enter Base: "))
exp_val = int(input("Enter Exp: "))
exponent(base_val, exp_val)
