def perfect(x):
    f = []
    for i in range(1, x):
        if x % i == 0:
            f.append(i)
    if sum(f) == x:
        return True
    else:
        return False


n = eval(input('请输入整数>>'))
print(perfect(n))
