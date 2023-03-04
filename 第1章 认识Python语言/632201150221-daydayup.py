#天天向上
dayup=(1.0+0.01)**365
daydown=(1.0-0.01)**365
print("您的基数从1开始:\n如果您每天努力，一年后您的基数为{:.2f}!\n如果每天放任，一年后您的基数为{:.2f}!\n您努力之后的基数是放任的{:.2f}倍！".format(dayup,daydown,dayup/daydown))