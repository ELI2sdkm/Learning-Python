# 从键盘输入一行字符，分别统计其中英文字母、空格、数字和其它字符的个数。
s = input('请输入一行字符：')
letters = 0
space = 0
digit = 0
others = 0

for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1

print('字母个数：%d' % letters)
print('空格个数：%d' % space)
print('数字个数：%d' % digit)
print('其他字符个数：%d' % others)
