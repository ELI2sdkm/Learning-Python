def ys(a, b, c):
    if c == '+':
        x = a + b
    elif c == '-':
        x = a - b
    elif c == '*':
        x = a * b
    elif c == '/' and b != 0:
        x = a / b
    else:
        x = '输入有误'
    return x
