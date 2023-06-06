# 计算1！+3！+4！+9！，编写函数实现阶乘功能。
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


nums = input("请输入多个数字，以空格分隔：")
num_list = [int(num) for num in nums.split()]

sum = 0
for num in num_list:
    sum += fact(num)
print(sum)
