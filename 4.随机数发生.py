# -*- coding: utf-8 -*-
"""
Created on Sat May  1 16:02:03 2021

@author: lenovo
"""
#本节记录随机数发生的方法，以及随机化部分数据(包括文本数据)的方法，总结了常见的几种随机数的发生方式。

import random
import string
import numpy as np

#随机数发生
print(random.randint(1,10) )  # 产生 1 到 10 的一个整数型随机数  
print(random.random() )       # 产生 0 到 1 之间的随机浮点数
print(random.uniform(1.1,5.4))#产生1.1到5.4之间的随机浮点数，区间可以不是整数
print(random.choice('tomorrow') )  # 从序列中随机选取一个元素
print(random.randrange(1,100,2) )  # 生成从1到100的间隔为2的随机整数
#乱序
a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
random.shuffle(a)
print(a)

# 随机整数：
random.randint(1,10)

# 随机选取0到100间的偶数：
random.randrange(0, 101, 2)

# 随机浮点数：
random.random()
random.uniform(1, 10)

# 随机字符：
random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')

# 多个字符中生成指定数量的随机字符：
random.sample('zyxwvutsrqponmlkjihgfedcba',5)

# 从a-zA-Z0-9生成指定数量的随机字符：
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
ran_str

# 多个字符中选取指定数量的字符组成新字符串：
''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))

# 随机选取字符串：
random.choice(['剪刀', '石头', '布'])

# 打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)

#使用random库生成特定分布的随机数：
##设置种子：seed
random.seed(1345)

##0到1之间随机浮点数
random.random()   

##均匀分布U(a, b)：浮点型
random.uniform(20,100)
random.uniform(100,20)

##正态分布N(mu, sigma)
random.normalvariate(0,2) #均值为0，标准差为2
random.gauss(0,2)

##指数分布
random.expovariate(5) #强度为5的指数分布

##########################################################################
#比较伤的是random包里只能生成一个，所以改用numpy库进行随机数生成
#均匀分布
np.random.uniform(1,10,20)#服从U(1,10)的20个均匀分布随机数

#几何分布
np.random.geometric(0.7, 20) #成功概率为0.7的20个几何分布随机数

#二项分布
np.random.binomial(100,0.7,20) #服从B(100,0.7)的20个二项分布随机数

#指数分布
np.random.standard_exponential(20) #20个标准指数分布随机数
np.random.exponential(3, 20)  #强度为3的20个指数分布随机数

#正态分布
np.random.standard_normal(20)#生成20个标准正态分布的随机数
np.random.normal(2, 4, 20) #均值为2，标准差为4的20个正态分布随机数

#卡方分布
np.random.chisquare(20, 20)#自由度为20的20个卡方分布随机数

#t分布
np.random.standard_t(6, 20)#自由度为6的20个t分布随机数

#F分布
np.random.f(25, 15, 20) #服从F(25,15)的20个F分布随机数

#泊松分布
np.random.poisson(4, 20) #强度为4的20个泊松分布随机数
