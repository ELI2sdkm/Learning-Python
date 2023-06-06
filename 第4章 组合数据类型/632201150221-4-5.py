# 统计并输出列表中包含的峰值个数。（若列表中的一个元素大于它的前后相邻元素，则该元素为一个峰值。）
ls = [33, 76, 89, 21, 10, 44, 57, 69, 28, 71]
n = 0
if ls[0] > ls[1]:
    n += 1
for i in range(1, len(ls)-1):
    if ls[i] > ls[i-1] and ls[i] > ls[i+1]:
        n += 1
if ls[len(ls)-1] > ls[len(ls)-2]:
    n += 1
print(n)
