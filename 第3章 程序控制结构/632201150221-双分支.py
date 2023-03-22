#编写代码，根据输入x的值，求y的值。
import math
x=eval(input('请输入x的值：'))
if x>=0:
    print('y=',math.sqrt(x))
else:
    print('y=',math.fabs(x)+10)