#日期和时间库的使用
import datetime
today = datetime.date.today()
a = datetime.date(1949, 10, 1)
print('新中国成立到今天共计{}天。'.format((today-a).days))
