# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:14:54 2021

@author: lenovo
"""


#常见数据类型
#整数型int
a = int(23)
print(type(a))

#浮点型float
b = float(23.5)
print(type(b))

#字符串str
c = "HELLO WORLD"
print(type(c))
len(c) #空格占用一个长度

#空值None
d = None  #
len(d) #None 不占用长度
type(d)#查看类型

#列表
#list：用中括号表示
e = ["a,B,c","df"]
len(e) #以元素个数计算长度
type(e) #查看类型
print(e) #输出全部内容

#对list的操作
list1 = [9, "北京", "GG", "114514", [114514, 1919810]]
len(list1)
type(list1)
print(list1)
