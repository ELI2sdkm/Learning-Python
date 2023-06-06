# 实验函数的定义和调用，请同学们在开发环境中输入以下代码，练习函数的定义和调用。
def happy():
    print('happy birthday to you!')


def hn(name):
    happy()
    happy()
    print('happy birthday ,dear {}!'.format(name))
    happy()


hn('Mike')
hn('Lily')
