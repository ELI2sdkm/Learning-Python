#输入一个正整数n，计算n的位数
n = abs(int(input("请输入一个正整数：")))
count = 0
while n > 0:
    count += 1
    n //= 10
print("这个数的位数是{}".format(count))