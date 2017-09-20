#!/usr/bin/env python
# -*-coding :uft-8 -*-
# Author:Anony

# 参考文档 http://egon09.blog.51cto.com/9161406/1840425

'''
时间的形式：
（1）时间戳
（2）格式化字串
（3）结构化元组形式
'''


# time模块
'''
import time

print(time.time())    # 输出时间戳，单位为s,始于1970.1.1，终于当前时间
t1 = time.gmtime()    # 将时间戳转换成元组形式的utc标准时间，不指定时间戳时，默认是当前时间戳
print(t1)
print(t1.tm_year)     # 输出元组中对应的元素值
t2 = time.localtime() # 将时间戳转换成元组形式的本地时间(utc+8)，不指定时间戳时，默认是当前时间戳
print(t2)
print(t2.tm_year)     # 输出元组中对应的元素值

print(time.asctime(t1)) # 将元组转换成字串
print(time.ctime(time.time())) # 将时间戳转换成字串
print(time.mktime(t1))
print(time.mktime(t2))  # 将元组形式转换成时间戳
print(time.strftime("%Y-%m-%d %H:%M:%S",t1))
print(time.strftime("%Y-%m-%d %H:%M:%S",t2))   # 将元组形式转换成格式字串
                                               # 该操作的本质是，获取t2元组中tm_year元素的值赋给%Y；以此类推
print(time.strptime("2017-09-12 21:16:19","%Y-%m-%d %H:%M:%S"))  # 将格式字串转换为元组形式，
                                                                 # 该操作的本质是：将%Y对应的值赋给tm_year；以此类推
time.sleep(3)  # 睡眠3秒
'''
# datatime模块是对time的进一步封装
'''
datatime主要有3个类：
datatime.data类：对年月日的操作
datatime.time类：对时分秒的操作
datatime.datatime：对年月日时分秒的操作
'''
import datetime
print(datetime.datetime.now())   # 获取当前时间
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间加3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间减3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间加3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=3))  # 当前时间加3分钟

















