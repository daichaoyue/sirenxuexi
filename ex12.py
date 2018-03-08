# -*- coding: utf-8 -*-
#向下注释
# raw_input函数的另一种用法，也是实用用法
# 直接在后面（）里面输出字符串，提示用户该输入什么。
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight) 
