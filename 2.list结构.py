# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:16:59 2021

@author: lenovo
"""

#本节主要针对list这一类型进行操作。


#提取list中元素
I = [1,2,3,4,5,6,7,8,9,10]
I[2:5]  #计数从0开始
I[-1]   #倒数第一个
I[-3]
I[:]   #输出全部

##提取字符串元素，以I为例
I[2] #也是从0开始

#list添加元素
I.append(7) #在尾部添加7
I
I.insert(0,9) #添加9到0号位置
I
I2 = [7, 7, 8]
I.extend(I2) #在I的末尾加上I2
I

#list删除元素(del,pop,remove)
del I[0] #删去0号位
I
I.pop(5) #去掉了第6位并显示去掉的元素
I.remove(7) #去掉了第一个7
I

#list元素替换
I[3] = "k" #3号位置替换为k
I

#list的运算
#list的“加法”
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b #相当于[a, b]
c

#list的乘法
a = ['haha']
d = a * 100
d

#判断元素是否在list中(in 或 not in)
a1 = ["小明", "Jane", "玛丽", "Lucy", "兰溪", "Mike", "强子"]
'Mike' in a1  #判断Mike是否在A1中
'Mike' not in a1

#list排序(sort)
#两种方法：sorted(list)和list.sort()
a2 = [8,123,9,7,7.8]
sorted(a2) #从小到大排列a2，对原来的a2不作改变
a2.sort()  #在a2上直接改动
a2

#list索引(index)、计数(count)、翻转(reverse)
l = ['a', 'b', 'c', 'd', 'b', 'b']
l.index('b') #第一个b出现在几号位置
l.count('b') #“b”出现了几次
l.reverse() #倒转序列l
l
x = l[::-1] #同样表示倒转
x

#list去重(set)
a = [1, 3, 2, 2, 1, 5, 7, 2]
b = set(a)
print(type(b))

#list补充
l = [1, 2, 3, 4, 5, 6]
l1 = [x for x in l]                      #遍历所有l中的元素，直接写入l1
l2 = [x * 2 for x in l]                  #遍历l中元素，乘2后写入l2
l3 = [x * 2 for x in l if x > 3]         #当x>3时乘2写入l3，其余不写入
l4 = [y * 2 for y in [x + 1 for x in l]] #将x中的元素加1，再乘2，写入l4

#list和str的相互转化
##str转化为list
s = "Stars , Cosmos , Gods , Animus , Antrum , Unbirth , Anima ,  Animsphere."
##全切分
l1 = list(s) #全切分，按照逐个字母、标点、空格完全分隔
l1
##按照空格(或其他符号)切分
l2 = s.split(' ') # 按照空格分割字符串
l2
##单词处理
x1 = "Animsphere"
x1.isalpha()  #检测字符串是否只由字母组成
x2 = x1.upper()  #全部大写
x2
x3 = x1.lower() #全部小写
x3
##字符替换
x4 = s.replace("Anima","Aniums") #将前一个字符替换为后一个字符
x4 = x4.replace("Animsphere","Animasphere")
x4
x5 = x4.split(",",) #去除""中的元素,转化为list
x5

#list转化为str
q = ["ss", "dsjkg", "fjk", "dsh", "fdshfs", "学生"]
q1 = ",".join(q)    #按照逗号拼接元素，转化为str
q1

