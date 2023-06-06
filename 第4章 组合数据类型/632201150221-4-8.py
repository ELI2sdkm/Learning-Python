# 求列表中元素的平均值、标准差和中位数。设列表值为：33, 76, 89, 21, 10, 44, 57, 69, 28, 71
ls = [33, 76, 89, 21, 10, 44, 57, 69, 28, 71]

s = 0
for x in ls:
    s += x
ave = s / len(ls)

for i in range(0, (len(ls))):
    sta = ((ls[i]-ave)**2 / len(ls))**(1/2)

ls.sort()
if len(ls) % 2 == 0:
    m1 = ls[len(ls)//2-1]
    m2 = ls[len(ls)//2]
    med = (m1 + m2) / 2
else:
    med = [len(ls)//2]

print("平均值： {}，标准差： {}，中位数： {}。".format(ave, sta, med))