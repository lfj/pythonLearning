#!/usr/bin/python
# -*- coding: UTF-8 -*-

#追加list
import math
list = ['a', 'b', 'c', 'd'];
list.append('e')
print list

list[len(list):] = ['f']
print list

#使用extenc方法可以将一个list追加到另一个列表上
list1 = [1, 2, '3', 4, 5]
list2 = ['a', 'b', 'c', 6, 7]
list1.extend(list2)
print list1