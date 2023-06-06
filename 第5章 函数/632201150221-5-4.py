# 书写程序求列表：[33, 76, 89, 21, 10, 44, 57, 69, 28, 71]中前3个、6个、全部元素的和。
def sum(list, n):
    s = 0
    for i in range(0, n):
        s += list[i]
    return s


li = [33, 76, 89, 21, 10, 44, 57, 69, 28, 71]
print(sum(li, 3), sum(li, 6), sum(li, len(li)))
