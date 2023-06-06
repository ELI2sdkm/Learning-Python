# 对列表[8,10,2,16,14,4,6,18,12]进行排序，然后中插入数值15，删除10。
li = [8, 10, 2, 16, 14, 4, 6, 18, 12]
li.sort()
print(li)
x = 15
for i in li:
    if i > x:
        ps = li.index(i)
        break
li.insert(ps, x)
print(li)
li.remove(10)
print(li)
