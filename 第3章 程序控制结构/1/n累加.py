i = 1
s = 0
k = eval(input())
while 1 / i >= 10 ** (-k):
    s += 1 / i
    i += 1
print(s)
