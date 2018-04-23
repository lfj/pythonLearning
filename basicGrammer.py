#!/usr/bin/python
# -*- coding: UTF-8 -*-
# python 基础语法
import time;  #引入time模块

print "你好，世界";
dict = {}
var1 = 1
del var1
s = 'ilovechina'
print s[0]
a = ['a', 'b', 'c']

ticks = time.time();
print "当前时间戳为", ticks

if True:
    print "True"
else:
    print "False"


# Python引号
word = 'word'
sentence = "这是一个句子"
paragraph = """这是一个段落包含了多个语句"""

# python注释
print "中国是一个伟大的国家"; #这是一个注释

'''
亚洲是世界上最大的洲
中国居于亚洲的中心，是中心之国
'''

"""
我是一个java程序员
但是我长期编写python代码
"""

#等待用户输入
# raw_input("按下 enter 键退出，其他任意键显示...\n")

#同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# print输出
x = 'a'
y = 'b'
# 换行输出
print x
print y

# 不换行输出
print x,
print y

# 不换行输出
print x,y


# 获取系统输入参数
import sys
# print sys.argv

#python pass语句
for letter in 'Python':
    if letter == 'h':
        pass
        print '这是 pass 块'
    print '当前字母：', letter

print "Good bye!"



count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1
print "Good bye!"








