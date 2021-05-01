# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:16:57 2021

@author: lenovo
"""
#本节记录python中常见的循环和判断语句。

import random

a = ["数学", "物理", "化学", "生物", "语文", "英语", "政治", "历史", "地理"]

#for循环
#第一种写法：直接对a中元素循环
for x in a:  #遍历a中的所有元素
  print(x)    #逐个打印a中的元素
  
#第二种写法：对a中元素所在位置进行循环
for i in range(len(a)):#按照位置编号遍历a中所有元素，从0开始，常用于对数循环
  print(a[i])
  
#第三种写法：enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中。
for i, item in enumerate(a):
  print(i, item)

#while循环：条件循环
#while循环即在满足某种条件的情况下进行循环，若不满足条件则停止循环。
i = 0
while(i<=5):    #输出0到6号
  print(a[i])
  i+=1


#判断语句：if else
#满足判断条件即执行某个命令，否则执行另外的命令
#if语句
gg = [0]*10#生成长度为10，元素为0的向量
for i in range(0,len(gg)):
  v = random.random()  #生成0到1之间随机的float型数据
  if v>0.5:
    gg[i] = 1  #模拟p=0.5的伯努利试验10次
print(gg)

#if else 语句：
gg1 = [0]*10#生成长度为10，元素为0的向量
for i in range(0,len(gg1)):
  v = random.random()
  if v>0.5:
    gg1[i] = 1  #模拟p=0.5的伯努利试验10次，成功记为1，失败记为-1
  else:
    gg1[i] = -1
print(gg1)

#if,elif,else语句：
gg2 = [0]*10#生成长度为10，元素为0的向量
for i in range(0,len(gg2)):
  v = random.random()
  if v<0.3:
    gg2[i] = 1  #多项分布
  elif v>0.5:
    gg2[i] = -1
  else:
    gg2[i] = 0
print(gg2)


#混合使用：while和判断语句的使用
#案例：判断奇数和偶数
test1 = [2,34,5,657,8,9,23,5,66,43,54]
odd = []   #记录奇数
even = []  #记录偶数
while len(test1)>0:  #数据集test1中还有元素则循环继续
  number = test1.pop()  #提取test1中最后一个元素
  if number%2 == 1:     #奇数
    odd.append(number)  #添加到odd
  else:                 #偶数
    even.append(number) #添加到even
odd
even
