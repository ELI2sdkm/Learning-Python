#输出当前时间和日期
import time
t_tuple = time.localtime()
print('当前时间元组：',t_tuple)
print('当前年：',t_tuple.tm_year)
print('当前月：',t_tuple.tm_mon)
print('当前日：',t_tuple.tm_mday)
print('当前时：',t_tuple.tm_hour)
print('当前分：',t_tuple.tm_min)
print('当前秒：',t_tuple.tm_mon)
print('当前周几：',t_tuple.tm_wday)
print('当前天数是一年中的：',t_tuple.tm_yday)
