#年龄(Age)小于24岁，三个预赛成绩的总分(Total)高于285分，其中有一个成绩为100分
age = 18
mark1 = 99
mark2 = 100
mark3 = 89
total = mark1 + mark2 + mark3
excellent = (age>285 and mark1==100 or mark2==100 or mark3==100)
print(excellent)