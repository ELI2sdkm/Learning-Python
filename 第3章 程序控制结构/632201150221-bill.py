#公用电话收费标准如下：通话时间在3分钟以内，收费0.5元；3分钟以上，则每超过1分钟加收0.15元。编写程序，输入通话分钟数，计算应缴电话费。
import math
t=eval(input('请输入通话时长（min）：'))
if t<0 :
    print('输入有误')
if 0<t<=3 :
    b=0.5
else :
    b=(t-3)*0.15
print('应缴电话费',round(b,2),'元')