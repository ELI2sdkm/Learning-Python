#请将以下代码转换为多分支结构语句。
x=eval(input('请输入x的值：'))
if 0<=x<=30:
    y=0,1,2,3
    if x<15:
        y=0,1
        if x<10:
            y=0
        else:
            y=1
    else:
        y=2,3
        if x<20:
                y=2
        else:
                y=3
    print('y=',y)
else:
    print('输入格式有误')