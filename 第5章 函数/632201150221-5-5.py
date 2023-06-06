# 实现multi()函数，参数个数不限，返回所有参数的乘积。
def multi(*t):
    s = 1
    for k in t:
        s *= k
    return s


print(multi(5, 6, 7))
