# -*- coding: utf-8 -*-
#建立函数 add （参数a，b） 冒号
def add(a, b):
#  打印  ADDING    a   b  的整数显示
	print "ADDING %d + %d" % (a, b)
	#返回值  a+b 
	return a + b

#建立函数 subtract（参数a，b） 冒号
def subtract(a, b):
# 打印  SUBTRACTING   a b 的整数显示 
	print "SUBTRACTING %d - %d" %(a, b)
	#返回值 a - b 
	return a - b

# 建立函数 multiply（参数a，b） 冒号
def multiply(a, b):
# 打印  MULTIPLYING a b 整数显示
	print "MULTIPLYING %d * %d " % (a, b)
	#返回值 a*b 
	return a * b 
	
#建立函数 （参数a，b） 冒号
def divide(a, b):
#打印 DIVIDE a b 的整数显示
	print "DIVIDE %d / %d" % (a, b)
	#返回值 a / b 
	return a / b 
	

#打印  让我们  做一些    数学
print "Let's do somemath with just functions!"

#定义变量 = 自建函数 add（参数30， 5）
# 这里使用函数时候直接打印自建函数 的print字符串
# age变量和下面其他变量力里面只保存了 return返回的值 
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#打印  上面刚定义的各种变量的整数显示，   后面（带入变量）
print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)


# 一个 难题  在这 额外的  学习   打字     无论如何
#A puzzle for the extra credit, type it in anyway.
#打印 这是一个难题
print "Here is a puzzle."

#定义变量 what = 第一个函数 add（参数age，第二个函数subtract（）的值做为add（）函数的参数
#subtract（参数height，multiply（）第三个函数的值做为 subtract函数的参数）
#multiply（参数wight， divide()函数的值做为 multiply函数的参数）
# divide（参数iq， 数值2）
#由内而外运算，先运行divide函数，然后往上层函数递归，
#或者可以理解 结束的）））） 的顺序运算，先运算第一个括号前，然后让下运算
#注意：每次调用一个函数赋值给 what的时候，会运行函数内部的运算
# 这个练习每个函数都先运算print语句，在返回值给函数本身，
#所以会由内而外运行每个函数的 print语句；并可以观察运行规则
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# 打印  既然如此， 变量what的值，你能动手做这个么？
print "That becomes: ", what, "Can you do it by hand?"