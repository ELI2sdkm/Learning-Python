# 随机产生26个英文字符，对其排序，再逆序输出。
import random

s = []
for i in range(1,100):
    x = random.randint(97,122)
    if chr(x) not in s:
        s.append(chr(x))
    if len(s) == 26:
        break
s.sort(reverse=True)
print(s)
