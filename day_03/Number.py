#!/usr/bin/env python
# coding: utf-8

"""
数字
@version: 1.0
@author: duanchao
@license: Apache Licence 
@file: Number.py
@time: 2017/9/6 16:53
"""
var1 = 1
var2 = 10
var3 = 100

### 删除对象的引用
del var1
del var2, var3
# print var1  # 这段会报错, 因为var1已经被删除

print 'var1' in dir()           # 判断变量是否存在
print locals().has_key('var1')  # 判断变量是否存在





