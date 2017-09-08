#!/usr/bin/env python
# coding: utf-8

"""
字符串
@version: 1.0
@author: duanchao
@license: Apache Licence 
@file: String.py
@time: 2017/9/6 17:54
"""
var1 = 'hello world'
var2 = 'python runoob'

print var1[0]
print var1[1:5]

print var1[:6] + 'runoob'
print var1 * 2

#######################################################################
## Python 转义字符
########################## \  换行符  #################################
var1 = 'hello' \
    ' world'
print var1
######################### \ 转义 ######################################
print '\\ \' \" \a   ds\b \e \000 \n \v \t \r \f \o12 \x12'
## \a    响铃
## \b    退格
## \e    转义
## \000  空
## \n    换行
## \v    纵向制表符
## \t    横向制表符
## \r    回车
## \f    换页
## \oyy  八进制数
## \xyy  十六进制数


print 'h' in 'hello'
print 'h' not in 'hello'
print r'\n', R'\''

######################### 字符串格式化 ######################################
print 'My name is %s and age is %d!' % ('dc', 18)

## %c     格式化字符及其ASCII码
## %s     格式化字符串
## %d     格式化整数
## %u     格式化无符号整型
## %o     格式化无符号八进制数
## %x     格式化无符号十六进制数
## %X     格式化无符号十六进制数(大写)
## %f     格式化浮点数字, 可指定小数点后的精度
## %e     用科学计算法格式化浮点数
## %E
## %g / %G   %f 和 %e 的简写
## %p     用十六进制数格式化变量的地址

print 'ASCII码: %c'              % (102)
print '无符号整型: %u'           % (1)
print '无符号八进制数: %o'       % (9)
print '无符号十六进制数: %x'     % (15)
print '浮点数: %f'                % (2.33)



#######################################################################
## Python 三引号（triple quotes）
######################################################################
hi = '''hi
there'''

print hi
print repr(hi)


###### Unicode 字符串
print u'hello\u0020world'





########################################################################
## Python 三引号（triple quotes）                                     #
######################################################################

print 'asd'.capitalize()                         # 字符串的第一个字符大写
print 'string'.center(10)                        # 返回一个原字符串居中, 并使用空格填充至长度10的新字符串
print 'hello world'.count('l',0, 10)            # 0-10内字符出现的次数
print 'hello'.decode('UTF-8', 'strict')        # 以指定格式解码 (UTF-8 可不传, 默认), 后面的strict 可不传(默认值),如果出错会默认报一个ValueError的异常
print 'hello'.encode('UTF-8')                   # 以指定格式编码 (UTF-8 可不传, 默认),

## endwith
## find
## format
## index
## isalnum     判断字符串是否全为字母或数字
print 'a'.isalnum()
print 'a2'.isalnum()
print ''.isalnum()
print '_'.isalnum()
## isalpha     判断字符串是否全为字母
## isdecimal   判断字符串是否只包含十进制数字(必须是Unicode字符串)
## isdigit     判断字符串是否只包含数字
print '321312321312312.1231'.isdigit()
## islower
## isnumeric   判断是否只包含数字字符, (必须是Unicode字符串)
print u'321312321'.isnumeric()
## isspace     字符串只包含空格返回true
##...
## lower
print 'HELLO WORLd'.lower()
## split
print 'hello world wtf !'.split(' ', 2)
## upper
print 'hello World'.upper()
print u'213212a'.isdecimal()







