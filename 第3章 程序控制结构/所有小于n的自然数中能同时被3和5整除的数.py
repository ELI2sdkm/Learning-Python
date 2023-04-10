#输入一个正整数n，找出所有小于n的自然数中能同时被3和5整除的数
n = int(input("请输入一个正整数："))
i = 1
while i < n:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1