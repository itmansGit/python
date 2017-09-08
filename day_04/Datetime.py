#!/usr/bin/env python
# coding: utf-8

"""
日期和时间
@version: 1.0
@author: duanchao
@license: Apache Licence 
@file: Datetime.py
@time: 2017/9/7 16:46
"""
import time;   # 引入time模块

ticks =time.time()
print '当前时间戳为:', ticks


##########   时间元组
## 0    tm_year     4位数字         2017
## 1    tm_mon      月              1-12
## 2    tm_mday     日              1-31
## 3    tm_hour     时              0-59
## 4    tm_min      分钟            0-59
## 5    tm_sec      秒              0-61 (60或61 是闰秒)
## 6    tm_wday     一周的第几日    0 到 6 (0是周日)
## 7    tm_yday     一年的第几日    1 到 366 (儒略历)
## 8    tm_isdst    夏令时          -1, 0, 1, -1 是决定是否为夏令时的旗帜

localtime = time.localtime(time.time())
print "本地时间为:", localtime

asctime = time.asctime(localtime)
print "标准时间:", asctime


# 格式化成2017-09-07 17:58:38形式 (其中 Y 大写格式为 2017 , 小写格式为 17)
formattime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print "格式化时间: ", formattime

# 格式化成Sat Mar 28 22:24:24 2016形式 (其中 Y 大写格式为 2017 , 小写格式为 17)
print "格式化时间:", time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式化时间字符串转换为时间戳
a = "Thu Sep 07 18:05:55 2017"
print "strptime : ",time.strptime(a, "%a %b %d %H:%M:%S %Y")
print "mktime : ",time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))


# python 中时间日期格式化符号
# %y 两位数的年份表示 ( 00-99 )
# %Y 四位数的年份表示 (000-9999)
# %m 月份 (01-12)
# %d 月内中的一天 (0-31)
# %H 24小时制小时数 (0-23)
# %l 12小时制小时数 (01-12)
# %M 分钟数 (00-59)
# %S 秒 (00-59)
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天 (001-366)
# %p 本地
# %U 一年中的星期数 (00-53) 星期天为星期的开始
# %w 星期(0-6), 星期天为星期的开始
# %W 一年中的星期数 (00-53) 星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

################## Calendar
import calendar;

cal = calendar.month(2017, 2)
print "以下输出2017年1月份的日历"
print cal


time.sleep(1)
print "线程休眠了10秒"


# 1000 为 1970 年后经过的时间
print time.localtime(1000)

# 1970年后经过的时间
print time.time()


############################################################################
## Calendar
############################################################################
# 打印某一年的日历, 3个月一行
print calendar.calendar(2017)

# 返回当前每周起始日期的设置
print calendar.firstweekday()

# 是闰年返回True，否则为false。
print calendar.isleap(2017)

# 返回在Y1，Y2两年之间的闰年总数
print calendar.leapdays(2017, 2060)

# 某一月的日历
print calendar.month(2017, 1)

# 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数
print "monthcalendar", calendar.monthcalendar(2017, 2)

# 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码
print calendar.monthrange(2017, 9)

# 等同于 calendar.calendar(year,w,l,c).
print calendar.prcal(2017)

# 等同于 calendar.month
print calendar.prmonth(2017, 9)

# 设置每周的其实日期码
calendar.setfirstweekday(1)
print calendar.firstweekday()

















