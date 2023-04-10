#输入一个正整数n，求1到n的阶乘之和
n = int(input("请输入一个正整数："))
sum = 0
i = 1
while i <= n:
    factorial = 1
    j = 1
    while j <= i:
        factorial *= j
        j += 1
    sum += factorial
    i += 1
print("1到{}的阶乘之和为{}".format(n,sum))