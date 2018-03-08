# -*- coding: utf-8 -*-
# 向下注释
# x = 这有 %d（10） 种 人   % 变量
x = "There are %d types of people." % 10
#二进制 定义变量
binary = "binary"
#不行 定义变量
do_not = "don't"
#   这有懂 %s（binary，第一个变量）  和 这有 %s（do_not，第二个变量）   （变量名一，变量名二）
y = "Those who know %s and those who %s." % (binary, do_not)
# 打印 变量X
print x
# 打印 变量y
print y 

#打印 “我 说 %r（编译字符串显示） 带入第一个变量x
print "I said : %r." % x 
#打印 “我 还 说 %s（用户字符串显示） 带入第一个变量y
print "I also said: '%s'" % y 
#令人捧腹的 =假 不成立
hilarious = False
#笑话 评价。。。=这个 笑话不好笑吗？%r（编译字符串显示）“
joke_evaluation = "Isn't that joke so funny?! %r"

# 打印 变量  % 另一个变量（这里被前一个带入了，看第一个变量的最后%字符）
print joke_evaluation % hilarious 

# 定义变量w =这是左边说的。。。
w = "This is the left side of..."
# 定义变量e = 这个字符串在右边说
e = "a string with a right side."

# 打印变量w加e， 字符串用+操作符是直接把两个字符串话合成一个字符串
print w + e 