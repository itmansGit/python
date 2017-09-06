#!/usr/bin/env python
# encoding: utf-8

"""
条件语句
@version: 1.0
@author: duanchao
@license: Apache Licence 
@file: condition.py
@time: 2017/9/6 14:31
"""
####################################################################################################################
## if else / if elif ... else
####################################################################################################################
if_flag = True          # True / False 首字母必须大写

if if_flag:
    print 'true'
else:
    print 'false'

a = 10
if (a > 10) :
    print 'a > 10'
elif (a == 10) :
    print 'a == 10'
else:
    print 'a < 10'

if (a >= 0 and a <= 5) or (a >= 10 and a <= 15) :
    print 'a 在0~5 或 10~15 之间'

####################################################################################################################
## while
####################################################################################################################
count = 0           
while (count < 9):
    print 'The count is:', count
    count = count + 1
  
print "Good bye!"


### continue  break
count = 0
while (count < 9):
    count = count + 1
    if (count == 2):
        continue
    print 'The count is :', count

count = 0
while (count < 9) :
    count = count + 1              
    if (count == 5):
        break
    print 'The count is    :', count


### while...else
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"


####################################################################################################################
## for
##
## 语法
## for iterating_var in sequence:
##   statements(s)
####################################################################################################################
for letter in 'python':
    print '当前字母 : ', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print '当前水果 : ', fruit

for index in range(len(fruits)):
    print '当前水果 : ', fruits[index]


for num in range(10, 20):
    for i in range(2, num):
        if num%i == 0:
            j = num / i
            print '%d 等于 %d * %d' % (num,i,j)
            break
    else:
        print num, '是一个质数'



####################################################################################################################
## pass   空占位符
####################################################################################################################

pass




