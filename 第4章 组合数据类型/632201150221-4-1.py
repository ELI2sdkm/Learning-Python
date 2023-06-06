#  随机产生100个[70,100]之间数据，找出75第一次出现的位置，并统计其出现的次数。
import random

li = []
for i in range(0, 100):
    x = random.randint(70, 100)
    li.append(x)
    print(li[i], end=" ")
    if (i + 1) % 10 == 0:
        print()
find_number = (75)
print(find_number)
print('第一次出现的位置：', li.index(find_number))
print('出现次数：', li.count(find_number))
