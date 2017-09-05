#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: duanchao
@license: Apache Licence 
@file: Hello.py
@time: 2017/9/4 14:33
"""
print "你好 世界";

if True:
    print "True"
else:
    print "False"
    print "False"


time_one = 1
time_two = 2

total = time_one + \
        time_two

print total

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday"]

print days[0]

word = '这是一段文字'
sentence = "这是一个句子"
paragraph = '''这
是一个段落'''

print paragraph


# 这是一个注释
print "hello"; # 这也是一个注释

name = "ccc" # 这还是一个注释

'''
这是一个多行注释
'''

"""
这还是一个多行注释
"""


raw_input('\n\nPress the enter key to exit.')

import sys; x = "0001"; sys.stdout.write(x)

x = 'a'
y = 'b'
print x
print y

print '-----------'

# 不换行输出
print x,
print y

var1 = 1
var10 = 10
del  var1
print var1

