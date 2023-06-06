# 请将输入的10个学生的成绩，计算其平均值并统计超过平均值的数据个数，并找出最接近平均值的元素。
li = list(eval(input()))
s = 0
n = 0
# 计算平均值
for i in li:
    s += i
ave = s/len(li)
# 统计超过平均值的数据个数
for i in li:
    if i > ave:
        n += 1
min_dif = abs(li[0] - ave)
p = 0
# 找出最接近平均值的元素
for i in li:
    dif = abs(i - ave)
    if dif < min_dif:
        min_dif = dif
        p = li.index(i)

print('平均数为{}，大于平均数的数据有{}个，最接近平均值的元素是{}。'.format(ave, n, li[p]))
