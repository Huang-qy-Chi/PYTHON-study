# -*- coding: utf-8 -*-
"""
Created on Fri May 14 10:29:54 2021

@author: lenovo
"""
#假设检验部分编程Python版本，作为与R版本的对照
#需要调用的库
import numpy as np
from scipy import stats   #scipy用于假设检验较多
import math


#一样本正态检验
##一样本方差已知Z检验:单边检验
###直接使用分位数进行假设检验
def ztest1(data, mu = 0, sigma = 1, alpha = 0.05):
    alpha1 = alpha
    meandata = np.mean(data) #均值
    n = math.sqrt(len(data))
    Z = n*(meandata - mu)/sigma #Z统计量
    if Z>stats.norm(0,1).ppf(1-alpha): #使用分位数确定拒绝域，ppf是逆累积分布函数，即alpha分位数
      print("Reject H0 at the significance level of", alpha1, ".")
    else:
      print("Accept H0 at the significance level of", alpha1, ".")

###测试
data = np.random.normal(0.1, 1, 100)
ztest1(data)
ztest1(data, mu = 0.1, sigma = 1, alpha = 0.01)

###使用p-value进行假设检验
####p-value是指原假设成立的情形下出现比观测更加“极端”情形的概率
def ztest2(data, mu = 0, sigma = 1):
    meandata = np.mean(data) #均值
    n = math.sqrt(len(data))
    Z = n*(meandata - mu)/sigma #Z统计量
    pvalue = 1 - stats.norm(0, 1).cdf(Z) #Z的累积分布，1减即为p-value：单边检验比Z更大即为更“极端”
    print("The p-value of the Z test is:", pvalue)

data1 = np.random.normal(1, 1, 100)
####更换不同的mu进行检验
ztest2(data1, mu = 0)
ztest2(data1, mu = 0.5)
ztest2(data1, mu = 0.95)
ztest2(data1, mu = 1)

###双侧Z检验：改变拒绝域，单侧变为双侧即可
def ztest3(data, mu = 0, sigma = 1, alpha = 0.05):
    alpha1 = alpha
    meandata = np.mean(data) #均值
    n = math.sqrt(len(data))
    Z = n*(meandata - mu)/sigma #Z统计量
    if Z>stats.norm(0,1).ppf(1-alpha/2) or Z<stats.norm(0,1).ppf(alpha/2):
      print("Reject H0 at the significance level of", alpha1, ".")
    else:
      print("Accept H0 at the significance level of", alpha1, ".")

ztest3(data, alpha = 0.01)


##未知方差情形下一样本t检验
###调用第三方库stats，进行一样本t检验
stats.ttest_1samp(data, 0)  #检验data均值与是否具有显著差异，返回t与p值

###编写直接t检验的函数，以单边检验为例，并直接输出p-value
def t_test1(data, mu = 0):
    meandata = np.mean(data) #均值
    n = math.sqrt(len(data))
    Sd = np.var(data)
    T = n*(meandata - mu)/Sd #T统计量
    pvalue = 1 - stats.norm(0, 1).cdf(T)
    print("The p-value of the t test is:", pvalue) #t值本身不直观就没输出了

t_test1(data, -0.05)


##卡方检验
###以双侧检验H0:sigma1=1为例
####构造拒绝域版本函数
def chisq1(data, sigma = 1, alpha = 0.05):
    alpha1 = alpha
    Sd = np.var(data)
    n1 = len(data)-1
    Chisq = n1*Sd/sigma
    if Chisq<stats.chi2(len(data)-1).cdf(alpha/2) or Chisq>stats.chi2(len(data)-1).cdf(1-alpha/2):
        print("Reject H0 at the significance level of", alpha1, ".")
    else:
        print("Accept H0 at the significance level of", alpha1, ".")

data2 = np.random.normal(0, 4, 100) #sigma真值为2
chisq1(data, sigma = 1.9, alpha = 0.01)



#两样本正态检验
##方差相等的均值t检验
data3 = np.random.normal(3, 1, 100)
data4 = np.random.normal(2, 1, 100)
data5 = np.random.normal(2, 2, 100)

###Python自带函数
####方差相等
stats.levene(data3, data4) #levene检验，检验方差齐性，p>alpha接受原假设：方差相等，与方差的F检验相同
stats.ttest_ind(data3, data4) #方差相等可以直接检验
####方差不等
stats.levene(data4, data5)
stats.ttest_ind(data4, data5, equal_var = False) #设置方差不等的参数

###自编写函数，双侧检验
def ttest2(data1, data2, alpha = 0.05, equals = "TRUE"):
    alpha1 = alpha
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    Sd1 = np.var(data1)
    Sd2 = np.var(data2)
    n1 = len(data1)
    n2 = len(data2)
    if equals == "TRUE":    #方差是否相等的参数，将两种情况整合为一个函数
        T = (mean1-mean2)/((n1**-1+n2**-1)*Sd1)
    elif equals == "FALSE":
        Sd = ((n1-1)*Sd1+(n2-1)*Sd2)/(n1+n2-2)
        T = (mean1-mean2)/((n1**-1+n2**-1)*Sd)
    if abs(T)>stats.t(n1+n2-2, 0, 1).ppf(1-alpha/2):
      print("Reject H0 at the significance level of", alpha1, ".")
    else:
      print("Accept H0 at the significance level of", alpha1, ".")

ttest2(data3, data4, alpha = 0.01, equals = "TRUE")
ttest2(data4, data5, alpha = 0.01, equals = "FALSE")


##方差的F检验
###Python中没有找到直接进行方差检验的函数，因此自行编写
###以双边假设为例
def ftest(data1, data2, alpha = 0.05):
    alpha1 = alpha
    Sd1 = np.var(data1)
    Sd2 = np.var(data2)
    n1 = len(data1)
    n2 = len(data2)
    F = Sd1/Sd2    #F统计量
    if F>stats.f(n1-1,n2-1).ppf(1-alpha/2) or F<stats.f(n1-1,n2-1).ppf(alpha/2):
      print("Reject H0 at the significance level of", alpha1, ".")
    else:
      print("Accept H0 at the significance level of", alpha1, ".")

ftest(data4, data5, alpha = 0.01)



#功效的模拟计算
##以单边方差已知的Z检验为例，通过随机模拟的方法计算功效。已知标准差为1，原假设mu=0，备择假设为mu>0，显著性水平为0.05
u = [0]*1000 #1000维向量，用于存储结果
for i in range(0,len(u)-1):  #区别于R，Python从0开始计数
    d = np.random.normal(0.1, 1, 100)  #生成数据，事实上均值为0.1
    n = math.sqrt(len(d))
    mean_d = np.mean(d)
    mu = 0
    sigma = 1
    alpha = 0.05
    Z = n*(mean_d - mu)/sigma  #Z统计量
    if Z>stats.norm(0,1).ppf(1-alpha):  #记录正确拒绝原假设的次数
        u[i] = 1
power = np.mean(u)    #用正确拒绝了原假设的频率近似估计功效
power



#Bootstrap版t检验举例：原假设为H0:X=Y=0，备择假设H1：X>Y
def boot_T(X, Y, alpha = 0.05, B = 1000): #X与Y保证均值相等，否则需要将均值修正到相等
    alpha1 = alpha
    meanX = np.mean(X)
    meanY = np.mean(Y)
    X = X - meanX  #处理序列均值相同
    Y = Y - meanY
    nX = len(X)
    nY = len(Y)
    SdX = np.var(X)
    SdY = np.var(Y)
    T_obs = (meanX-meanY)/math.sqrt(SdX/nX + SdY/nY)
    u = [0]*B
    for i in range(0,B):
        xb = np.random.choice(X, nX, replace = True) #不需要设置权重
        yb = np.random.choice(Y, nY, replace = True)
        meanx = np.mean(xb)
        meany = np.mean(yb)
        sdx = np.var(xb)
        sdy = np.var(yb)
        tb = (meanx-meany)/math.sqrt(sdx/nX + sdy/nY)
        if tb>T_obs:
            u[i] = 1
    p_value = np.mean(u)
    if p_value<alpha:
        print("Reject H0 at the significance level of", alpha1, ".")
    else:
      print("Accept H0 at the significance level of", alpha1, ".")

#测试函数
X = np.random.normal(0, 1, 100)
X1 = np.random.normal(1, 1, 100)
Y = np.random.normal(0, 1, 100)
boot_T(X, Y, 0.01, 2000)  #Bootstrap重复试验次数一般大于100，这里取2000
boot_T(X1, Y)