#编写代码计算“校园贷”在8个月后需要偿还多少钱，如果贷10000元，签订8个月的偿还期限，日利率为8‰。
capital=10000
interest=0.008
day=1
while day<=240 :
    capital*=(1+interest)
    day=day+1
print('应偿还：',capital,'元')