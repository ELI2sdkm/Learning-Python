# 编写代码，根据以下公式求e的近似值，当末项小于10的负五次方时停止计算。   e=1+1/1!+1/2!+1/3!+...+1/n!+...
import math
i = 1
e = 1
t = 1
while abs(1 / t) >= 10 ** (-5):
    t = math.factorial(i)
    e += 1 / t
    i += 1
print('结果为：', e)
