# 输出Fibonacci数列：1，1，2，3，5，8，……的前20项。(注：Fibonacci数列的定义如下：F(1)=1，F(2)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 3，n ∈ N*）)
a = 1
b = 1
print(a, end=' ')
print(b, end=' ')
for i in range(3, 21):
    c = a + b
    a = b
    b = c
    print(c, end=' ')
