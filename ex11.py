# -*- coding: utf-8 -*-
#向下注释
#打印，你多大了，后面， 用来连接下行
print "How old are you?",
#定义变量 age（年龄） = 输入函数  input（输入）
age = raw_input()
#打印 = 你多高 ？   ，
print "How tall are you?",
#定义变量height（身高）  =输入函数
height = raw_input()
#打印  多少       你   重量  ，
print "How much do you weight?",
#定义变量weight （体重） = 输入函数
weight = raw_input()

#打印  所以 你的 %r （带入第一个函数）大， %r（第二个函数） 高 和%r （第三个函数）重
# raw_input（） 获取用户输入，所以最后需要用户输入三次
# raw_input（） 在Python3 中已经简化为 input（）
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
