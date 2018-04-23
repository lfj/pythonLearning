#!/usr/bin/python
# -*- coding: UTF-8 -*-

#python 循环的使用方法

#the first method of using circle
countries = ['China', 'Japan', 'Korea', 'USA'];
"""
for country in countries:
    print '当前国家：', country
"""

#the second method of using circle
for index in range(len(countries)):
    print 'the current country is', countries[index]

#使用内置enumerate 函数进行遍历
languages = ['Chinese', 'Japanese', 'English']
for (i, j) in enumerate(languages):
    print i,j

numbers = [12, 3, 7, 6, 13]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print even
print odd











