x=eval(input('请输入你的生日：'))
y=eval(input('请输入母亲的生日：'))
z=eval(input('请输入父亲的生日：'))
for i in range(10000,999999) :
    if i%x==0 and i%y==0 and i%z==0 :
        break
# noinspection PyUnboundLocalVariable
print(i)