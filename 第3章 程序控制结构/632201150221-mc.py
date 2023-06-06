# 蒙特卡罗方法求解π，随机向单位正方形和圆结构，抛洒大量“飞镖”点；计算每个点到圆心的距离从而判断该点在圆内或者圆外；用圆内的点数除以总点数就是π/4值。
import random
import math

n = 0
for i in range(1, 10001):
    x = random.random()
    y = random.random()
    d = math.sqrt(x * x + y ** 2)
    if d <= 1:
        n += 1
pi = 4 * (n / 10000)
print('Pi的值是{}.'.format(pi))
